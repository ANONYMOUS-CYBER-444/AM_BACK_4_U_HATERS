import os, platform
os.system('git pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from TRY import main
    main()
elif bit == '32bit':
    from gift import main
    main()