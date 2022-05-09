class JsonNode:
    def __init__(self, key: str, val: str) -> None:
        self.key = key,
        self.val = val

    def __str__(self) -> str:
        # for some reason key is getting casted to a tuple
        return f'{self.key[0]}: {self.val}'



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