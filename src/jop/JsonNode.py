class JsonNode:
    def __init__(self, data=[]) -> None:
        # using a list to store this node data because it is ordered 
        self._data = data

    # TODO this must return a value
    def add_data(self, data) -> None:
        self._data.append(data)


    def __str__(self) -> str:
        output = "{"
        for e in self._data:
            if type(e) == KVPair:
                if e != self._data[0]:
                    output = output + ', ' + str(e)
                else:
                    output = output + str(e)
        output = output + "}"
        
        return output

class node:
    def __init__(
        self,
        key:str, 
        
        # value fields
        number_value:int=None,
        string_value:str=None,
        bool_value:bool=None,

        # link to other nodes
        parent=None, # used if this is a child object
        child=None, # used if this is a child object
        next=None, # used if there is more than one node in this layer
    ) -> None:
        self.key = key

        # point this node to itself if this is the only node in the layer
        if next == None:
            next = self



class KVPair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f'{self.key}: {self.value}'


# original implementation 
# struct JsonNode
# {
# 	/* only if parent is an object or array (NULL otherwise) */
# 	JsonNode *parent;
# 	JsonNode *prev, *next;
	
# 	/* only if parent is an object (NULL otherwise) */
# 	char *key; /* Must be valid UTF-8. */
	
# 	JsonTag tag;
# 	union {
# 		/* JSON_BOOL */
# 		bool bool_;
		
# 		/* JSON_STRING */
# 		char *string_; /* Must be valid UTF-8. */
		
# 		/* JSON_NUMBER */
# 		double number_;
		
# 		/* JSON_ARRAY */
# 		/* JSON_OBJECT */
# 		struct {
# 			JsonNode *head, *tail;
# 		} children;
# 	};
# };