# Code format:
- Code follows Python standard PEP8 format
- Monitor Size of objects: `sys.getsizeof(mylist)`
- Create progress bar:<br>
	`from progress.bar import Bar`<br>`
	bar = Bar('Processing', max=20)`<br>`  
	for i in range(20):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`   # Do some work`<br>&nbsp;&nbsp;&nbsp;&nbsp;`bar.next()`<br>`  
	bar.finish()`<br>

- Project Structure following [standard conventions](https://data-flair.training/blogs/python-best-practices/).

