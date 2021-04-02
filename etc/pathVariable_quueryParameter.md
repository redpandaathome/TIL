link: https://medium.com/@fullsour/when-should-you-use-path-variable-and-query-parameter-a346790e8a6d

# When should you use Path Variable, and how about Query Parameter?
As a best practice, almost of developers are recommending following way. If you want to identify a resource, you should use Path Variable. But if you want to sort or filter items, then you should use query parameter. So, for example you can define like this:
```
/users # Fetch a list of users
/users?occupation=programer # Fetch a list of programer user
/users/123 # Fetch a user who has id 123
```