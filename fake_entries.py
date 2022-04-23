import crypto
import database

database.initialize_connection()
key = crypto.convert_passphrase_to_key("1")

i = int(input("# "))

j = 0
while j < i:
    title = crypto.encrypt(f"Title #{j}", key)
    text = crypto.encrypt(f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id cursus felis. Nunc dolor libero, ultricies ut tellus non, vulputate vestibulum libero. Aenean mattis urna id nibh imperdiet rutrum. Duis a vestibulum eros. Vestibulum sed commodo est, non porta nisi. Fusce congue diam sed tellus vestibulum, et consectetur arcu molestie. Nam eu dolor quis ipsum malesuada gravida eget ac risus. Curabitur fermentum risus vel lectus imperdiet, eu auctor urna eleifend. Etiam odio quam, tincidunt sed consectetur a, finibus sodales justo. Maecenas non metus sed tellus porttitor commodo. Proin pretium arcu quis feugiat finibus. Donec efficitur ligula sit amet nisl suscipit cursus. Morbi nec ante et lorem feugiat tempor. Mauris faucibus maximus velit. Cras at est sapien. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sem eu enim tristique porttitor sit amet sit amet arcu. Sed in egestas tellus, nec molestie sapien. Cras venenatis eleifend leo, lobortis laoreet tellus vestibulum quis. Nam ut lorem orci. Vestibulum dui arcu, molestie at venenatis at, scelerisque nec libero. Donec eu sodales lorem. Aenean ac eros justo. Fusce id justo libero. Cras posuere nisl a sem lobortis malesuada. Duis vel eleifend quam. Etiam et libero lorem. Nullam sollicitudin massa eu libero semper, vitae tempor mauris tincidunt. Duis sodales eros purus. Donec eu bibendum massa. Curabitur feugiat et tellus vitae ullamcorper. Nullam eget pharetra velit. In malesuada ultricies sagittis. Cras tincidunt erat vitae accumsan scelerisque. Vivamus tempor feugiat nisl. Morbi cursus posuere semper. Donec blandit elementum justo, at eleifend quam molestie eget. Duis eget sem ligula. Cras enim nisi, hendrerit ut posuere ac, volutpat imperdiet risus. Donec vitae sapien nisl. Donec mattis augue id enim pellentesque euismod. Suspendisse aliquet tempus pretium.", key)
    database.create_entry(title, text)
    j += 1

database.close_connection()