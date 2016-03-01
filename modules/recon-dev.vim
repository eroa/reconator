let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/workspace/t28/reconator
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +34 parse.py
badd +53 libnmap.py
badd +0 ~/.vimrc
badd +1 modules/reconator.py
badd +1 reconator.py2
badd +6 reconator.py
badd +1 modules/scans.py
badd +1 modules/parse.py
badd +1 modules/results.py
badd +0 modules/tasks.py
badd +180 ~/workspace/t28/recon_scan/recon_scan/reconscan.py
argglobal
silent! argdel *
set stal=2
edit reconator.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
argglobal
enew
file NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/t28/reconator
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=pymode#folding#expr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((4 * winheight(0) + 23) / 47)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
tabedit ~/workspace/t28/recon_scan/recon_scan/reconscan.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
argglobal
enew
file ~/NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/t28/reconator
wincmd w
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 178 - ((24 * winheight(0) + 23) / 47)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
178
normal! 0
lcd ~/workspace/t28/recon_scan/recon_scan
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
tabedit ~/workspace/t28/reconator/modules/parse.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
argglobal
enew
file ~/NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/t28/reconator/modules
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=pymode#folding#expr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 11 - ((10 * winheight(0) + 23) / 46)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
11
normal! 011|
lcd ~/workspace/t28/reconator/modules
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
tabedit ~/workspace/t28/reconator/modules/results.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
argglobal
enew
file ~/NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/t28/reconator/modules
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=pymode#folding#expr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 23) / 47)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/workspace/t28/reconator/modules
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
tabedit ~/workspace/t28/reconator/modules/tasks.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
argglobal
enew
file ~/NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/t28/reconator/modules
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=pymode#folding#expr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 23) / 47)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/workspace/t28/reconator/modules
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
tabedit ~/workspace/t28/reconator/modules/scans.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe '2resize ' . ((&lines * 43 + 24) / 48)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
exe '3resize ' . ((&lines * 3 + 24) / 48)
exe 'vert 3resize ' . ((&columns * 79 + 55) / 111)
argglobal
enew
file ~/NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/t28/reconator/modules
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=pymode#folding#expr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 43 - ((27 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
43
normal! 0
lcd ~/workspace/t28/reconator/modules
wincmd w
argglobal
enew
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
lcd ~/workspace/t28/reconator/modules
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 55) / 111)
exe '2resize ' . ((&lines * 43 + 24) / 48)
exe 'vert 2resize ' . ((&columns * 79 + 55) / 111)
exe '3resize ' . ((&lines * 3 + 24) / 48)
exe 'vert 3resize ' . ((&columns * 79 + 55) / 111)
tabnext 3
set stal=1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filmnrxoOtT
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
