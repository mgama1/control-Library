# Pyctrl

Pyctrl is an open source modern control library

## Features
- state space to transfer function 
- tranfer function to state space 
- System Solution
- Controlability
- Observability
- Stabillity
- Stepresonse
- Pole placement 

## Dependencies 
- numpy
- sympy
- mpmath
- matplotlib


## Documentation

<div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">importing:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="kn">from</span> <span class="nn">pyctrl</span> <span class="kn">import</span> <span class="o">*</span>
<span class="n">pyc</span><span class="o">=</span><span class="n">pyctrl</span><span class="p">()</span>
</pre>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

# convertion from state space to transfer function[¶](#convertion-from-state-space-to-transfer-function)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In </div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">A</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">10</span><span class="p">],[</span><span class="mi">5</span><span class="p">,</span><span class="mi">2</span><span class="p">]])</span>
<span class="n">B</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">C</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">])</span>
<span class="n">D</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">0</span><span class="p">])</span>

<span class="n">pyc</span><span class="o">.</span><span class="n">ss2tf</span><span class="p">(</span><span class="n">A</span><span class="p">,</span><span class="n">B</span><span class="p">,</span><span class="n">C</span><span class="p">,</span><span class="n">D</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out:</div>

<img src="https://latex.codecogs.com/svg.image?\frac{s&plus;8}{s^2-5s-44}" title="\frac{s+8}{s^2-5s-44}" />
</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

# conversion from transfer function to state space[¶](#conversion-from-transfer-function-to-state-space)

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

the default is the controllble form

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In :</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">n</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">4</span><span class="p">])</span>
<span class="n">d</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">10</span><span class="p">])</span>

<span class="n">pyc</span><span class="o">.</span><span class="n">tf2ss</span><span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="n">d</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out:</div>

<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">

<pre>(array([[  0.,   1.],
        [-10.,  -2.]]),
 array([0., 1.]),
 array([0., 4.]),
 array([0.]))</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In :</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">pyc</span><span class="o">.</span><span class="n">tf2ss</span><span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="n">d</span><span class="p">,</span><span class="s2">"observable"</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out:</div>

<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">

<pre>(array([[  0., -10.],
        [  1.,  -2.]]),
 array([0., 4.]),
 array([0., 1.]),
 array([0.]))</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

## solution of a system[¶](#solution-of-a-system)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In :</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">A</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">10</span><span class="p">],[</span><span class="mi">5</span><span class="p">,</span><span class="mi">2</span><span class="p">]])</span>
<span class="n">B</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">x0</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">])</span>
<span class="n">u</span><span class="o">=</span><span class="mi">1</span>

<span class="n">pyc</span><span class="o">.</span><span class="n">solve</span><span class="p">(</span><span class="n">A</span><span class="p">,</span><span class="n">B</span><span class="p">,</span><span class="n">x0</span><span class="p">,</span><span class="n">u</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out:</div>

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}\frac{s^{2}&space;-&space;s&space;&plus;&space;8}{s&space;\left(s^{2}&space;-&space;5&space;s&space;-&space;44\right)}&space;\\&space;\\&space;&space;\frac{2&space;\left(3&space;s&space;&plus;&space;1\right)}{s&space;\left(s^{2}&space;-&space;5&space;s&space;-&space;44\right)}\end{matrix}" title="\begin{matrix}\frac{s^{2} - s + 8}{s \left(s^{2} - 5 s - 44\right)} \\ \\ \frac{2 \left(3 s + 1\right)}{s \left(s^{2} - 5 s - 44\right)}\end{matrix}" />

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

# checking for stability, observability, and controllability[¶](#checking-for-stability,-observability,-and-controllability)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [12]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">A</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">10</span><span class="p">],[</span><span class="mi">5</span><span class="p">,</span><span class="mi">2</span><span class="p">]])</span>
<span class="n">B</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">C</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">])</span>
</pre>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

stability

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [13]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">pyc</span><span class="o">.</span><span class="n">isStable</span><span class="p">(</span><span class="n">A</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[13]:</div>

<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">

<pre>True</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

observability

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [14]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">pyc</span><span class="o">.</span><span class="n">isObservable</span><span class="p">(</span><span class="n">A</span><span class="p">,</span><span class="n">C</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[14]:</div>

<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">

<pre>True</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

controllability

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [15]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">pyc</span><span class="o">.</span><span class="n">isControllable</span><span class="p">(</span><span class="n">A</span><span class="p">,</span><span class="n">B</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out:</div>

<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">

<pre>True</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

# step response of the system[¶](#step-response-of-the-system)

</div>

</div>


<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In :</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">pyc</span><span class="o">.</span><span class="n">step</span><span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="n">d</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">
Out:
<div class="jp-OutputArea-child">
 
<img src="https://i.imgur.com/nHAlehO.png " />

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

# Pole placplacement[¶](#Pole-placplacement)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In :</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">A</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">],[</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span><span class="o">-</span><span class="mi">3</span><span class="p">,</span><span class="o">-</span><span class="mi">5</span><span class="p">]])</span>
<span class="n">B</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>

<span class="n">pyc</span><span class="o">.</span><span class="n">placePoles</span><span class="p">(</span><span class="n">A</span><span class="p">,</span><span class="n">B</span><span class="p">,</span><span class="o">-</span><span class="mi">4</span><span class="o">+</span><span class="mi">3</span><span class="n">j</span><span class="p">,</span><span class="o">-</span><span class="mi">4</span><span class="o">-</span><span class="mi">3</span><span class="n">j</span><span class="p">,</span><span class="o">-</span><span class="mi">4</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[8]:</div>

<img src="https://latex.codecogs.com/svg.image?\begin{vmatrix}98.0&space;&54.0&space;&space;&&space;7.0&space;\\\end{vmatrix}&space;" title="\begin{vmatrix}98.0 &54.0 & 7.0 \\\end{vmatrix} " />

</div>

</div>

</div>

</div>

## Contributing

Contributions are always welcome!

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mgama1)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/MgamalR)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  

