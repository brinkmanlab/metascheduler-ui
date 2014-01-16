import env

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*w(pe#@pwvibqoq1djtlk7p%qwy%!9my!p3p!w2+-7uy^d7@-4'

if env.TEST_ENV:
    DATABASE_USER = 'scheduler'
    DATABASE_PASSWORD = 'sched44%'
    DATABASE_HOST = 'mysql1'
elif env.PROD_ENV:
    DATABASE_USER = 'scheduler'
    DATABASE_PASSWORD = 'sched44%'
    DATABASE_HOST = 'mysql1'
else:
    DATABASE_USER = 'scheduler'
    DATABASE_PASSWORD = 'sched44%'
    DATABASE_HOST = 'localhost'

DATABASE_PORT = '3306'
