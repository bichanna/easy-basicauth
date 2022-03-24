# easy-basicauth


## Installation
```bash
pip install easy-basicauth
```

## Usage
It's very easy to use.
Just add `@basic_auth_required` just above your function name.
> **NOTE**: You should add `user` as one of the parameters.
```python
from basicauth.decorator import basic_auth_required

@basic_auth_required
def some_view(request, user):
	pass
```

In case you prefer classes to functions:
```python
class SomeClass(View):
  @basic_auth_required
  def get(request, user):
    pass
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
[MIT](https://github.com/bichanna/django-basicauth/blob/master/LICENSE)
