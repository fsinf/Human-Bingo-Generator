#!/usr/bin/env python3

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
import random
import argparse
from datetime import datetime

title_text = "Human Bingo/Free drink game"
center_cell_text = "<b>Find \"someone\" who ...</b>"
description_text = """
<b>How does it work?</b><br></br> 
To get a free drink, you need to find people who have done something mentioned in a cell. 
The best way to find people is to talk to them. 
<br></br>
<br></br>
When you have 5 cells in a row, you can redeem your free drink. 
The middle cell is a joker and can be included in a row.
"""

list_of_strings = [
"is studying defaultInf",
"is studying SE",
"is studying TI/CE",
"is studying MediaInf",
"is studying MedicineInf",
"is studying VisualInf",
"is studying BI",
"is studying any MasterInf",
"studied something before",
"studies because their parents wanted them to",
"studies because their parents didnt want them to",
"has gotten a study grant",
"is almost done with their bsc",
"has a sister",
"has a brother",
"has more than 3 siblings",
"has a cat",
"has a dog",
"has uncommon pets",
"lives in Vienna",
"lives outside of Vienna",
"is vegetarian",
"is vegan",
"doesnt drink alcohol",
"hasn't eaten today yet",
"has gotten their bingo drink",
"has NOT gotten their bingo drink yet",
"paid with Mattermost today",
"is holding an etut",
"attends 3+ different etuts this semester",
"contributed to some open source project",
"uses only Linux",
"uses mastodon",
"uses a non-stock OS on their phone",
"uses a non android and non apple phone",
"has hugged THAT_TREE",
"knows sign language",
"has voted in öh elections",
"has contributed to VoWi",
"has 2000+ posts on Mattermost",
"has reacted to the MM-Announcement-post",
"follows @fsinf_at (insta)",
"follows @THAT_TREE_wien (insta)",
"owns a car",
"owns a bike",
"owns 3+ laptops",
"works for a living",
"goes bouldering",
"hates pizza",
"loves pineapples on pizza",
"has less than 5 plastic cards in their purse",
"goes running",
"goes skiing/snowboarding",
"goes windsurfing/kite surfing",
"plays factorio",
"can approximate 2^34",
"can approximate 2^37",
"can approximate 2^33",
"has arrived before 19:00",
"has arrived after 19:00",
"carries a powerbank with them",
"is from .de",
"is from .it",
"is from .ch",
"is from .sk",
"is from .cz",
"is from .hu",
"is from .uk",
"is from .us",
"is using Arch Linux",
"is using Debian",
"is using Ubuntu",
"is using GNU/Hurd (or an uncommon Linux Distro)",
"is using Gentoo",
"is using Fedora",
"is using OpenSUSE",
"knows the Free Software song",
"owns a physical server",
"is renting a (virtual-) server",
"owns a NAS",
"has backups",
"has recovered with backups",
"has suffered from dataloss -> missing backups",
"was at the top of St. Stephen (Vienna)",
"was at Cobenzl View Platform (Vienna)",
"was at the top of Donauturm (Vienna)",
"was at Donauinsel (Vienna)",
"has a ThinkPad",
"has a Framework Laptop",
"doesn't like coffee",
"does work next to their studies",
"does selfhost an Own-/Nextcloud instance",
"does selfhost a Git server",
"does selfhost an E-Mail server",
"doesn't use WhatsApp",
"disassembled their Laptop",
"disassembled their Phone"
]

def generate_pdf(output_filename, num_pages=1):
    random.seed()

    page_width, page_height = landscape(A4)
    table_size = 5
    cell_size = 70
    cell_size = 70

    c = canvas.Canvas(output_filename, pagesize=landscape(A4))
    
    styles = getSampleStyleSheet()
    title_style = styles['Title']

    table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.transparent),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ])

    cell_style = ParagraphStyle(name="CELL_STYLE", wordWrap = "LTR", alignment=TA_CENTER)

    center_cell_style = ParagraphStyle(name="CENTER_CELL_STYLE", wordWrap = "LTR", alignment=TA_CENTER)

    description_style = ParagraphStyle(name="DESCRIPTION_STYLE", wordWrap = "LTR", alignment=TA_LEFT)

    site_margin = 10
    frame_height = page_height - 2*site_margin
    frame_width = page_width/2 - 2*site_margin
    frame_left_x = site_margin
    frame_left_y = site_margin
    frame_right_x = page_width/2 + site_margin
    frame_right_y = site_margin

    for _ in range(num_pages):
        frame_left = Frame(frame_left_x, frame_left_y, frame_width, frame_height, showBoundary=False)
        frame_right = Frame(frame_right_x, frame_right_y, frame_width, frame_height, showBoundary=False)

        title = Paragraph(title_text, title_style)
        title_spacer = Spacer(1, 20)

        left_table_content = random.sample(list_of_strings, table_size*table_size)
        left_table_data = [[Paragraph(left_table_content[i * table_size + j], cell_style) for j in range(table_size)] for i in range(table_size)]

        right_table_content = random.sample(list_of_strings, table_size*table_size)
        right_table_data = [[Paragraph(right_table_content[i * table_size + j], cell_style) for j in range(table_size)] for i in range(table_size)]

        # Set the predefined string in the middle cell (position 2,2 in a 0-indexed 5x5 table)
        left_table_data[2][2] = Paragraph(center_cell_text, center_cell_style)
        right_table_data[2][2] = Paragraph(center_cell_text, center_cell_style)

        left_table = Table(left_table_data, colWidths=cell_size, rowHeights=cell_size)
        right_table = Table(right_table_data, colWidths=cell_size, rowHeights=cell_size)

        left_table.setStyle(table_style)
        right_table.setStyle(table_style)

        description_spacer = Spacer(1, 20)

        description = Paragraph(description_text, description_style)
    
        frame_left.addFromList([title, title_spacer, left_table, description_spacer, description], c)
        frame_right.addFromList([title, title_spacer, right_table, description_spacer, description], c)

        # add page to canvas
        c.showPage()

    
    c.save()


# Set up argument parsing
parser = argparse.ArgumentParser(description="Generate a drinking bingo with specified number of pages and frames.")
parser.add_argument("-f", "--file", type=str, required=True, help="Output PDF file name (e.g., output.pdf)")
parser.add_argument("-n", "--number", type=int, required=True, help="Number of pages in the PDF")

# Parse arguments
args = parser.parse_args()


generate_pdf(args.file, args.number)
