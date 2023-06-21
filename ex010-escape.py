import html
string_original = "<script>alert(1)</script>"
string_escape = html.escape(string_original)
# Exibindo o resultado
print("String original: {}".format(string_original))
print("String escapada: {}".format(string_escape))

