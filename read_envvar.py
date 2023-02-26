import os

# Windows:
print (os.environ['USERNAME'])

# Linux
print (os.environ['USER'])

# Error Handeling 
print (os.environ.get['FOO'])
print (os.getenv('FOO', 'Test'))
