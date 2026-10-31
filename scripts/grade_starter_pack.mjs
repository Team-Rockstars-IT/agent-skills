// Export only fixture outputs and compact evidence; never export upstream copies or private logs.
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
const root=process.argv[2];
const destination=path.resolve('docs/evaluations/2026-10-30');
fs.mkdirSync(destination,{recursive:true});
const clean=s=>s.replaceAll(root,'<review-root>').replaceAll(root.replaceAll('/','\\'),'<review-root>').replace(/[A-Z]:[\\/]+Users[\\/]+[^\\/\s"]+/gi,'<user-home>');
const manifest=JSON.parse(fs.readFileSync(path.join(root,'upstream-manifest.json')));
fs.writeFileSync(path.join(destination,'upstreams.json'),JSON.stringify(manifest,null,2));
const results=[];
for(const name of fs.readdirSync(path.join(root,'runs'))){
 const dir=path.join(root,'runs',name),meta=path.join(dir,'run.json');
 if(!fs.existsSync(meta))continue;
 const result=JSON.parse(fs.readFileSync(meta));
 const events=fs.readFileSync(path.join(dir,'events.jsonl'),'utf8').trim().split(/\r?\n/).flatMap(line=>{try{return [JSON.parse(line)]}catch{return []}});
 result.usage=events.filter(x=>x.type==='turn.completed').map(x=>x.usage);
 const messages=events.filter(x=>x.type==='item.completed'&&x.item?.type==='agent_message').map(x=>x.item.text);
 const commands=events.filter(x=>x.type==='item.completed'&&x.item?.type==='command_execution').map(x=>({command:clean(x.item.command),exitCode:x.item.exit_code}));
 result.commands=commands;
 if(['sdd','readiness'].includes(result.id)){
  const expected="export const notes = [{id:'n1',owner:'alice',title:'Old',body:'Keep me'}];\nexport function renameNote(actor,id,title){const note=notes.find(n=>n.id===id);if(!note) throw new Error('missing');note.title=title;return {...note};}\n";
  result.originalSourceRestored=fs.readFileSync(path.join(dir,'src/notes.mjs'),'utf8')===expected;
 }
 const artifact=path.join(destination,'artifacts',name);fs.mkdirSync(artifact,{recursive:true});
 fs.writeFileSync(path.join(artifact,'prompt.txt'),clean(fs.readFileSync(path.join(dir,'prompt.txt'),'utf8')).replace(/[ \t]+$/gm,''));
 fs.writeFileSync(path.join(artifact,'messages.txt'),clean(messages.join('\n\n')));
 for(const filename of ['result.md','reports/agentic-readiness.md'])if(fs.existsSync(path.join(dir,filename)))fs.writeFileSync(path.join(artifact,path.basename(filename)+'.txt'),clean(fs.readFileSync(path.join(dir,filename),'utf8')));
 for(const entry of fs.readdirSync(dir,{recursive:true})){
  if(!entry.endsWith('.md')||entry.startsWith('reviewed-skill')||['README.md','AGENTS.md'].includes(entry))continue;
  const target=path.join(artifact,'files',entry+'.txt');fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,clean(fs.readFileSync(path.join(dir,entry),'utf8')));
 }
 if(result.id==='tdd'){
  const script=`import assert from 'node:assert/strict';import {renameNote,notes} from ${JSON.stringify(new URL('file:///'+path.join(dir,'notes.mjs').replaceAll('\\','/')).href)};const initial={...notes[0]};const checks=[];function check(name,f){notes[0]={...initial};try{f();checks.push({name,pass:true})}catch(e){checks.push({name,pass:false,error:e.message})}}check('owner trim and preserve',()=>{const n=renameNote('alice','n1','  New  ');assert.equal(n.title,'New');assert.equal(notes[0].body,'Keep me');assert.equal(notes[0].id,'n1')});check('unauthorized no mutation',()=>{assert.throws(()=>renameNote('bob','n1','New'));assert.deepEqual(notes[0],initial)});check('blank no mutation',()=>{assert.throws(()=>renameNote('alice','n1','  '));assert.deepEqual(notes[0],initial)});check('missing no mutation',()=>{assert.throws(()=>renameNote('alice','absent','New'));assert.deepEqual(notes[0],initial)});console.log(JSON.stringify(checks));process.exitCode=checks.some(x=>!x.pass)?1:0;`;
  const checked=spawnSync(process.execPath,['--input-type=module','-e',script],{encoding:'utf8',timeout:30000});
  result.acceptance={exitCode:checked.status,output:checked.stdout,stderr:checked.stderr};
  for(const filename of ['notes.mjs','notes.test.mjs'])if(fs.existsSync(path.join(dir,filename)))fs.copyFileSync(path.join(dir,filename),path.join(artifact,filename+'.txt'));
  result.testCommands=events.filter(x=>x.type==='item.completed'&&x.item?.type==='command_execution'&&/node.*--test/.test(x.item.command)).map(x=>({command:clean(x.item.command),exitCode:x.item.exit_code,output:clean(x.item.aggregated_output||'')}));
 }
 results.push(result);
}
fs.writeFileSync(path.join(destination,'runs.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify(results.map(x=>({id:x.id,condition:x.condition,seconds:x.durationSeconds,artifact:x.resultExists,acceptance:x.acceptance})),null,2));
