from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from year_progress_percentage import year_progress_percentage


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def gradient_background(img_size, start_color, middle_color, end_color):
    base = Image.new('RGB', img_size)
    start_rgb = [int(start_color[i:i+2], 16) for i in (1, 3, 5)]
    middle_rgb = [int(middle_color[i:i+2], 16) for i in (1, 3, 5)]
    end_rgb = [int(end_color[i:i+2], 16) for i in (1, 3, 5)]

    for y in range(img_size[1]):
        t = y / img_size[1]
        if t < 0.5:
            t *= 2
            color = lerp_color(start_rgb, middle_rgb, t)
        else:
            t = (t - 0.5) * 2
            color = lerp_color(middle_rgb, end_rgb, t)
        for x in range(img_size[0]):
            base.putpixel((x, y), color)

    return base


def create_rounded_rectangle_mask(size, radius):
    """Create a mask for a rounded rectangle."""
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + size, fill=255, radius=radius)
    return mask


def create_progress_image(percentage):
    width, height = 1080, 1080

    # Create a new gradient background image
    img = gradient_background((width, height), "#59c173", "#a17fe0", "#5d26c1")
    draw = ImageDraw.Draw(img)

    # Draw the progress bar with reversed gradient
    bar_width = width * 0.8
    bar_height = 60
    border_thickness = 5
    bar_x, bar_y = int((width - bar_width) / 2), int((height - bar_height) / 2)

    # Border
    draw.rounded_rectangle([bar_x-border_thickness, bar_y-border_thickness, bar_x + bar_width +
                           border_thickness, bar_y + bar_height+border_thickness], fill="#2C5364", radius=bar_height/2)

    # Background
    draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_width,
                           bar_y + bar_height], fill="#2C5364", radius=bar_height/2)
    buffer = 5
    fill_width = int(bar_width * (percentage / 100))

    progress_bar = gradient_background(
        (int(bar_width), int(bar_height)), "#DA22FF", "#9733EE", "#2C5364")
    mask = create_rounded_rectangle_mask(
        (int(fill_width), int(bar_height)), bar_height/2)

    img.paste(progress_bar.crop((0, 0, fill_width, bar_height)),
              (bar_x, bar_y), mask)

    # Load a font
    font_path = "fonts/BricolageGrotesque.ttf"
    font_size = 100
    font = ImageFont.truetype(font_path, font_size)

    # Draw the year and percentage text
    year = datetime.now().year
    text = f"{year} está {percentage:.0f}% completo"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    margin = 40
    text_x, text_y = int((width - text_width) /
                         2), int(bar_y - text_height - margin)
    draw.text((text_x, text_y), text, font=font, fill="white")

    # Save the image
    filename = f'progress_{percentage:.0f}' + ".jpeg"
    img.save(f'generated_images/{filename}', 'JPEG')


# Usage
percentage = year_progress_percentage()
create_progress_image(percentage)
