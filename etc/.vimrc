"自动缩进
set autoindent
set smartindent

"tab 宽度 与转换
set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab

"显示行号
set number
"行号宽度为2
set numberwidth=2
"显示相对行号
set relativenumber

"高亮匹配的括号
set showmatch


"窗口分割时,进行切换的按键热键需要连接两次,比如从下方窗口移动
"光标到上方窗口,需要<c-w><c-w>k,非常麻烦,现在重映射为<c-k>,切换的
"时候会变得非常方便.
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l


" 终端显示256色
set t_Co=256

" 在搜索的时候忽略大小写
set ignorecase

" 设定默认解码
set encoding=utf-8
set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set fileencodings=utf-8,ucs-bom,chinese

