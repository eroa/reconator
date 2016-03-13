let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/workspace/reconator/core
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +28 nmapscan.py
badd +53 reconator.py
badd +1 ~/workspace/reconator/draft/NmapParser.py
badd +1 ~/workspace/reconator/draft/startnmap.py
badd +6 ~/workspace/reconator/draft/parser.py
badd +1 ~/workspace/reconator/draft/NmapPortCount.py
badd +1 ~/workspace/reconator/reconator-dev.py
badd +2 ~/workspace/reconator/draft/libnmap_scan_n_parse.py
badd +0 ~/NERD_tree_1
argglobal
silent! argdel *
edit nmapscan.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
argglobal
enew
file NERD_tree_2
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/reconator/core
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
let s:l = 28 - ((25 * winheight(0) + 22) / 45)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
28
normal! 017|
lcd ~/workspace/reconator/core
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
tabedit ~/workspace/reconator/core/reconator.py
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd t
set winheight=1 winwidth=1
exe '1resize ' . ((&lines * 42 + 23) / 47)
exe '2resize ' . ((&lines * 2 + 23) / 47)
argglobal
setlocal fdm=expr
setlocal fde=pymode#folding#expr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 53 - ((34 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
53
normal! 0
lcd ~/workspace/reconator/core
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
lcd ~/workspace/reconator/core
wincmd w
exe '1resize ' . ((&lines * 42 + 23) / 47)
exe '2resize ' . ((&lines * 2 + 23) / 47)
tabedit ~/workspace/reconator/draft/NmapParser.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
argglobal
enew
file ~/NERD_tree_2
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/reconator/draft
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
let s:l = 1 - ((0 * winheight(0) + 22) / 45)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/workspace/reconator/draft
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
tabedit ~/workspace/reconator/draft/libnmap_scan_n_parse.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
argglobal
enew
file ~/NERD_tree_2
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/reconator/draft
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
let s:l = 2 - ((1 * winheight(0) + 22) / 45)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
2
normal! 0
lcd ~/workspace/reconator/draft
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
tabedit ~/workspace/reconator/draft/parser.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
argglobal
enew
file ~/NERD_tree_2
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/workspace/reconator/draft
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
let s:l = 6 - ((5 * winheight(0) + 22) / 45)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
6
normal! 06|
lcd ~/workspace/reconator/draft
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 94) / 188)
exe 'vert 2resize ' . ((&columns * 156 + 94) / 188)
tabnext 2
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=1 shortmess=aoO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
