# Code format:
- Code follows Python standard PEP8 format
- Monitor Size of objects: `sys.getsizeof(mylist)`
- Create progress bar:<br>
	`from progress.bar import Bar`<br>`
	bar = Bar('Processing', max=20)`<br>`  
	for i in range(20):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`   # Do some work`<br>&nbsp;&nbsp;&nbsp;&nbsp;`bar.next()`<br>`  
	bar.finish()`<br>

- Project Structure following [standard conventions](https://data-flair.training/blogs/python-best-practices/).
- The code also practises *type-hinting*, even though
- Recursively remove pycache directories: `find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf`

# Code conventions:
- Discourage creation of single library or single constants file (Harder to maintain)
- Discouraged unecessary logging 
- Until doing something with error, no need to have try and catches
- Tests verified with following [asserts](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)

