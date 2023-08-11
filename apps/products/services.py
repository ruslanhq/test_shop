from django.http import HttpResponse

from openpyxl import Workbook


def export_products_to_excel(products):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Products'

    headers = [
        "ID", "Name", "Description", "Price", "Created At", "Category Name", "Tags"
    ]
    sheet.append(headers)

    for product in products:
        tags = ", ".join(tag.name for tag in product.tags.all())
        row = [
            product.id, product.name, product.description, product.price,
            product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            product.category.name, tags
        ]
        sheet.append(row)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'
    workbook.save(response)
    return response
