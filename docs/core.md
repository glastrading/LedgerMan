# Core

Here are some central features of LedgerMan that apply to every object / class.

## Serialization

LedgerMan uses [JCDB](https://github.com/glastrading/jcdb) for serialization - every object implemented by LedgerMan can be encoded to JSON by calling `object.encode()`. To decode objects from JSON strings, call `class.decode(string)` on the class you want to be decode an object of.

The JSON format storage used in JCDB works like this:

```python
# create a serializable object (of any kind)
o = Object()

# interact with the object (step is not required but common)
o.key = "value"
o.subObject = Object()

# serialize
print(o.encode())
```

This prints the following JSON string:

```
{
	"_type": "Object",
    "key": "value"
    "subObject": {
    	"_type": "Object"
    }
}
```

You can also export all objects to files `object.encodeToFile(fileName)` and import them again using `class.decodeFile(fileName)`.
