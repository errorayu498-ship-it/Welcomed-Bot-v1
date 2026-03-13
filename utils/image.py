from PIL import Image, ImageDraw, ImageFont
import io
from utils.cache import get_image
from utils.badges import get_badge_icons

async def create_card(member, config):

    width = 1100
    height = 500

    user = await member.guild.fetch_member(member.id)

    banner_url = None
    if user.banner and config["background_mode"] == "banner":
        banner_url = user.banner.url

    if banner_url:
        banner_data = await get_image(banner_url)
        bg = Image.open(io.BytesIO(banner_data)).resize((width,height))
    else:
        bg = Image.new("RGB",(width,height))
        draw = ImageDraw.Draw(bg)

        for y in range(height):
            r = int(60 + y/height*120)
            g = int(20 + y/height*160)
            b = int(120 + y/height*80)
            draw.line([(0,y),(width,y)],fill=(r,g,b))

    draw = ImageDraw.Draw(bg)

    avatar_data = await get_image(member.display_avatar.url)
    avatar = Image.open(io.BytesIO(avatar_data)).resize((260,260)).convert("RGBA")

    mask = Image.new("L",(260,260),0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0,0,260,260),fill=255)

    bg.paste(avatar,(60,120),mask)

    try:
        font_big = ImageFont.truetype("arial.ttf",65)
        font_small = ImageFont.truetype("arial.ttf",35)
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    title = config["title"].replace("{user}", member.name)
    subtitle = config["subtitle"].replace("{membercount}", str(member.guild.member_count))

    draw.text((380,120), title, fill=config["text_color"], font=font_big)
    draw.text((380,220), subtitle, fill=config["text_color"], font=font_small)

    badges = get_badge_icons(member)

    x = 380
    for badge in badges:
        try:
            icon = Image.open(badge).resize((50,50))
            bg.paste(icon,(x,320),icon)
            x += 60
        except:
            pass

    buffer = io.BytesIO()
    bg.save(buffer,"PNG")
    buffer.seek(0)

    return buffer