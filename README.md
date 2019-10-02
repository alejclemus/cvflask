# cvflask
 Web app with my curriculum vitae

<h2>Python</h2>

```bash
pip install -r requirements.txt

python main.py
```

<h2>Docker</h2>

You can build the image, and run it as

```bash
docker build --rm -f "Dockerfile" -t name:latest .

docker run -it -p 5000:5000 name:latest