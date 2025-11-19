The main concern is how to migrate / tranlsate / implement the Latex source into your web / HTML / CSS format.
We wonder if some of the features which are essential for a mathematics oriented text, and fully supported in Latex, will be supported by Pressbooks.

Such features are listed here:

1. Equations wth number, consistent with chapter (1.1, 1.2, ... for chapter 1, 2.1, 2.2, ... for chapter 2, etc)

At the moment, I was able to get equations numbered by writing them within ```\[\]``` delimiters.
```
\[
\mu = \frac{1}{N} \sum_{i = 1}^{N} x_{i} \; .
\]
```

And adding the following chunk to the CSS custom styles, in the `Appearance` section of Pressbooks.
```
/* Equations */
.equation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1.25rem auto;
  max-width: 80%;
}

.equation .MathJax, 
.equation mjx-container {
  flex-grow: 1;
  text-align: center;
}

.eq-number {
  font-size: 1em;
  color: inherit;
  margin-left: 1rem;
  white-space: nowrap;
}
```

2. Equations need to be able to be referenced Refer equations automatically, similar to
```
\begin{equation}
	\bar{x} = \frac{1}{n} (x_{1} + x_{2} + ... + x_{n}) \; .
	\label{eq:sample_mean1}
\end{equation}
```
```
And now we refer to our former equation \eqref{eq:sample_mean1}, ...
```

3. Figure captions with number, consistent with chapters, same problem as with equations.

4. Refer figures automatically, consistent with chapter numbers, same problem as with equations.

5. Flexible location of figures and their captions / labels.

6. At the moment, figures display in very blurred / pixelled format.

6. Some way to add a bibliograpy file (like a .bib for Latex) that would add the references, again, in an organzed way.
