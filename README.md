# slides

As my supervisor at Argonne once said, the job of a scientist is to "get good
data and make pretty pictures". This means dynamic and professional
presentations, even on short time tables.  Unfortunately, there are manifold
factors that make this difficult for scientists (and anybody, really).  First,
there's the fact that usually we are taking data until 4:39am the morning before
the presentation.  Secondly, there's all the different choices for
presentations.  Do I use `reveal.js`? Do I write it in LaTeX? Do I just use
Powerpoint?  And these lead to other questions for how others will review the
problems.  Finally, there's the problem of exporting.  If I have videos, how do
I export this to a pdf?  How high resolution do my plots need to be?  To solve
(some) of these problems, `slides` was created.  `slides` is a template engine
that allows you to write presentations in `markdown`.  It targets:

- [ ] Simple (and accurate) conversion from the `markdown` files to `reveal.js`,
  `pdflatex`, and Powerpoint presentations.
- [ ] LaTeX math supported
- [ ] bibtex bibliography supported
- [ ] video inclusion with still file for `pdflatex` export
- [ ] build system that watches data and rebuilds a plot if the data or plotting
  updates
- [ ] vector plot files (where possible)
