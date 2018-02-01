## Instructions
1. Clone repository
2. Create a new virtual environment using Python 3.4
3. Activate your virtual environment `source virt_env_path/bin/activate`
4. By the terminal navigate to the clone rope and dnstall requirements.txt
5. In terminal/console run `python app.py `
6. Test the Web API with the following url: http://127.0.0.1:5000/regions 
7. You should get the following json:
```
{
    regions: [
        "England",
        "Scotland",
        "UK",
        "Wales"
    ]
}
```