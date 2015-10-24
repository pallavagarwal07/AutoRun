if !has('python')
  echo "You need python compiled for liveupdate to work."
  finish
endif

function LiveUpdate()
  pyfile ../python/liveupdate.py
endfunc
