from flask import Flask, jsonify, request

app = Flask(__name__)

snippets = [
    {
      "id": 1,
      "language": "Python",
      "code": "print('Hello, World!')"
    },
    {
      "id": 2,
      "language": "Python",
      "code": "def add(a, b):\n    return a + b"
    },
    {
      "id": 3,
      "language": "Python",
      "code": "class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n\n    def area(self):\n        return 3.14 * self.radius ** 2"
    },
    {
      "id": 4,
      "language": "JavaScript",
      "code": "console.log('Hello, World!');"
    },
    {
      "id": 5,
      "language": "JavaScript",
      "code": "function multiply(a, b) {\n    return a * b;\n}"
    },
    {
      "id": 6,
      "language": "JavaScript",
      "code": "const square = num => num * num;"
    },
    {
      "id": 7,
      "language": "Java",
      "code": "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"
    },
    {
      "id": 8,
      "language": "Java",
      "code": "public class Rectangle {\n    private int width;\n    private int height;\n\n    public Rectangle(int width, int height) {\n        this.width = width;\n        this.height = height;\n    }\n\n    public int getArea() {\n        return width * height;\n    }\n}"
    }
]

#retrieve all snippets / by id / by code
@app.route('/snippets', methods = ['GET'])
def get_snippets():
  return jsonify(snippets)

@app.route('/snippets', methods = ['POST'])
def add_snippet():
  New_Item = request.json 
  New_Item['id'] = len(snippets) + 1 # (increases id by one more than the length) 
  snippets.append(New_Item)
  return jsonify(New_Item)


@app.route('/snippets', methods = ['PATCH'])
def update_snippet(item_id):
  updates = request.json
  for item in snippets:
    if item['id'] == item_id:
      item.update(updates)
      break
  return jsonify(item)

if __name__ == '__main__':
  app.run(debug=True) 


# The requests when using Postman should look like this
               
# GET (read)

# for a get request simple change the method to GET and type http://127.0.0.1:5000/snippets
# !!! IMPORTANT !!! - 'snippets' will differ based on your database/array name

# POST (create)

# Change the method to POST but keep the link the same
# Click body and type in what you want to add !! ID auto increments !!
# !!! IMPORTANT !!! - You must use "" and NOT '' as otherwise your code will not work 
# Example:
# {
#   "language": "Javascript"
#   "code": "print('Hello World!')"
# }

# PATCH (update)

# Change the method to PATCH. Take the link and add a /num depending on the ID you wish to update:
# http://127.0.0.1:5000/snippets/1 - updates the object with an ID of 1 etc 
# !!! IMPORTANT !!! - You must use "" and NOT '' as otherwise your code will not work 
# Example:
# {
#  "language": 'C#'
#  "code": 'Console.WriteLine("Hello World!");'
# }
 