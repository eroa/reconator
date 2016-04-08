let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +52 git/reconator/core/reconatoor-dev.py
badd +25 git/reconator/core/tests/grep-dev.py
badd +1 git/reconator/inspiration/recon_scan/recon_scan/ftprecon.py
badd +0 git/reconator/inspiration/recon_scan/recon_scan/reconscan.py
argglobal
silent! argdel *
set stal=2
edit git/reconator/core/reconatoor-dev.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winheight=1 winwidth=1
exe '1resize ' . ((&lines * 49 + 25) / 51)
exe 'vert 1resize ' . ((&columns * 68 + 94) / 188)
exe '2resize ' . ((&lines * 49 + 25) / 51)
exe 'vert 2resize ' . ((&columns * 119 + 94) / 188)
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
let s:l = 91 - ((3 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
91
normal! 0
lcd ~/git/reconator/inspiration/recon_scan/recon_scan
wincmd w
argglobal
edit ~/git/reconator/inspiration/recon_scan/recon_scan/reconscan.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 109 - ((3 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
109
normal! 04|
lcd ~/git/reconator/inspiration/recon_scan/recon_scan
wincmd w
exe '1resize ' . ((&lines * 49 + 25) / 51)
exe 'vert 1resize ' . ((&columns * 68 + 94) / 188)
exe '2resize ' . ((&lines * 49 + 25) / 51)
exe 'vert 2resize ' . ((&columns * 119 + 94) / 188)
tabedit ~/git/reconator/core/tests/grep-dev.py
set splitbelow splitright
wincmd t
set winheight=1 winwidth=1
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
let s:l = 25 - ((24 * winheight(0) + 25) / 50)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
25
normal! 021|
lcd ~/git/reconator/core/tests
tabnext 2
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
