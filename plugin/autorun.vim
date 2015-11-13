if !has('nvim')
  echo "You need neovim for autorun to work."
  finish
endif

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! AutoRun()
  execute 'pyfile '.s:path."/autorun.py"
endfunction


command! AutoRun call AutoRun()
