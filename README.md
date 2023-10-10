# basedjangoapp
alias migrate="python manage.py makemigrations;python manage.py migrate"
alias serve="python manage.py runserver"


from django.db.models import Sum, F

# Query to calculate the total price for each product
product_list = Product.objects.annotate(
    total_price=Sum(F('order__quantity') * F('price'), distinct=True)
)

# Print the result
for product in product_list:
    print(f"Product: {product.name}, Total Price: {product.total_price}")


ffmpeg -i Steins_Gate_-_S01E25_OVA.mkv -c:v h264 -hls_time 60 -hls_list_size 0 -hls_segment_filename segment%d.ts index.m3u8

faster conversion

# Convert MKV to HLS
ffmpeg -i "$input_file" -c:v libx264  -vf "scale=640:-1" -b:v 512k -preset ultrafast -threads 4 -hls_time 120 -hls_list_size 0 -hls_segment_filename "${output_dir}/${output_name}_%03d.ts" "${output_dir}/${output_name}.m3u8"

echo "HLS conversion completed. HLS files are located in: $output_dir"
