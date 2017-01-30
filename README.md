# slides

As my supervisor at Argonne once said, the job of a scientist is to "get good
data and make pretty pictures". This means dynamic and professional
presentations, even on short time tables.  Unfortunately, there are myriad
factors that make this difficult for scientists (and anybody, really).  First,
there's the fact that usually we are taking data until 4:39am the morning before
the presentation.  Secondly, there's all the different choices for
presentations.  Do I use `reveal.js`? Do I write it in LaTeX? Do I just use
Powerpoint?  And these lead to other questions for how others will review the
presentation.  Does my advisor want to use the "Track Changes" option in
powerpoint?  Is he or she too stubborn to learn anything else?  Does the team
want to mark it up in red pen on a printed pdf?  Finally, there's the problem of
exporting.  If I have videos, how do I export this to a pdf?  How high
resolution do my plots need to be?  To solve (some) of these problems, `slides`
was created.  `slides` is a template engine that allows you to write
presentations in `markdown` (mostly vanilla).  It targets:

-   Simple (and accurate) conversion from the `markdown` files to `reveal.js`,
  `pdflatex`, and Powerpoint presentations.
-   LaTeX math supported
-   bibtex bibliography supported
-   Write in markdown (or modified markdown)
-   Run code during conversion (with ipython or knitr?)
-   video inclusion with still file for `pdflatex` export
-   build system that watches data and rebuilds a plot if the data or plotting
  updates
-   vector plot files (where possible) for pdf export, d3 or other interactive
  plot files for web export
-   slide types:  
    -   title slide
    -   chapter title slide
    -   one column slide
    -   two column slide
    -   two column shift right
    -   two column shift left
    -   two row
    -   two row top two column
    -   two row bottom two column
    -   two row left sidebar
    -   two row right sidebar
    -   two row two column
    -   bibliography


## Example

It may be best to first show an example of how this would be used

```markdown

# Title of the presentation here
&author=Alex Hagen &&author
&subtitle=An example of how to use markdown to reveal.js/python/powerpoint
  conversion

--- &twocolumn
# Title of the slide

+++ &column
## Title of the column

- Some bullet points
- Some more bullet points

+++ &column

&chart=something.svg

--- &tworow
# Title of the slide

+++ &row
## Title of the row

- Bullet here
- Bullet here

+++  &row

[ &python &caption=some caption here
import pym
data = np.read_csv('somefile.csv')
plot = plot.something()
plot.show()
]

```
