To restart postgresql@9.5 after an upgrade:
  brew services restart postgresql@9.5
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/postgresql@9.5/bin/postgres -D /usr/local/var/postgresql@9.5


If you need to have postgresql@9.5 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/postgresql@9.5/bin:$PATH"' >> ~/.zshrc

>>> from signup import db 
>>> db.create_all()