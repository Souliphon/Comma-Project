"""django_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from members import views as member_views
from bookorder import views as bookorder_views
from booktype import views as booktype_views
from borrow import views as borrow_views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('date_return_out/', borrow_views.date_return_out, name='date-return-out'),
    path('book_over_borrow/', borrow_views.book_over_borrow, name='book-over-borrow'),
    path('book_over_borrow_pdf/', borrow_views.book_over_borrow_pdf, name='book-over-borrow-pdf'),
    path('book_over_borrow_bill/<int:pk>/', borrow_views.book_over_borrow_bill, name='book-over-borrow-bill'),


    # borrow urls
    path('export_borrow_book/', borrow_views.export_borrow_book, name='export-borrow-book'),

    path('borrow_book_list/', borrow_views.borrow_book_list, name='borrow-book-list'),
    path('borrow_book_update/<int:pk>/', borrow_views.borrow_book_update, name='borrow-book-update'),

    path('cut_point/<int:pk>', member_views.cut_point, name='cut-point'),
    path('select_point/', member_views.select_point, name='select-point'),

    path('borrow_list/', borrow_views.borrow_list, name='borrow-list'),
    path('borrow_update/<int:pk>/', borrow_views.borrow_update, name='borrow-update'),
    path('borrow_delete/<int:pk>/', borrow_views.borrow_delete, name='borrow-delete'),
    path('borrow_detail/<int:pk>/', borrow_views.borrow_detail, name='borrow-detail'),
    path('borrow_pdf/', borrow_views.borrow_pdf, name='borrow-pdf'),
    path('borrow_bill/<int:pk>/', borrow_views.borrow_bill, name='borrow-bill'),


    path('book_return_borrow/', borrow_views.book_return_borrow, name='book-return-borrow'),
    path('book_return_update/<int:pk>/', borrow_views.book_return_update, name='book-return-update'),


    # Book Return 
    path('book_return_create/', borrow_views.book_return_create, name='book-return-create'),
    path('book_return_list/', borrow_views.book_return_list, name='book-return-list'),
    path('return_update/<int:pk>/', borrow_views.return_update, name='return-update'),
    path('book_return_delete/<int:pk>/', borrow_views.book_return_delete, name='book-return-delete'),
    path('export_book_return/', borrow_views.export_book_return, name='export-book-return'),
    path('book_return_pdf/', borrow_views.book_return_pdf, name='book-return-pdf'),
    path('book_return_bill_pdf/<int:pk>/', borrow_views.book_return_bill_pdf, name='book-return-bill-pdf'),


    #reclaom book
    path('reclaim_book_create/', borrow_views.reclaim_book_create, name='reclaim-book-create'),
    path('reclaim_book_list/', borrow_views.reclaim_book_list, name='reclaim-book-list'),
    path('reclaim_book_update/<int:pk>/', borrow_views.reclaim_book_update, name='reclaim-book-update'),
    path('reclaim_book_delete/<int:pk>/', borrow_views.reclaim_book_delete, name='reclaim-book-delete'),
    path('reclaim_book_pdf/', borrow_views.reclaim_book_pdf, name='reclaim-book-pdf'),
    path('reclaim_bill_pdf/<int:pk>/', borrow_views.reclaim_bill_pdf, name='reclaim-bill-pdf'),
    path('export_reclaim_book/', borrow_views.export_reclaim_book, name='export-reclaim-book'),



    path('check_out_borrow_list/', borrow_views.check_out_borrow_list, name='check-out-borrow-list'),
    path('check_out_borrow_detail/<int:pk>/', borrow_views.check_out_borrow_detail, name='check-out-borrow-detail'),
    path('check_out_borrow_create/', borrow_views.check_out_borrow_create, name='check-out-borrow-create'),
    # path('bill_pdf_template/<int:pk>/', BillPDFView.as_view(), name='bill'),
    path('check_out_borrow_update/<int:pk>/', borrow_views.check_out_borrow_update, name='check-out-borrow-update'),

    path('borrow_bill_pdf/<int:pk>/', borrow_views.borrow_bill_pdf, name='borrow-bill-pdf'),



    # members urls
    path('members_list/', member_views.member_list, name='members-list'),
    path('members_view_more/', member_views.member_view_more, name='members-view-more'),
    path('members_create/', member_views.members_register, name='members-create'),
    path('members_update/<int:pk>/', member_views.member_update, name='members-update'),
    path('members_delete/<int:pk>/', member_views.member_delete, name='members-delete'),
    path('member_detail/<int:pk>/', member_views.member_detail, name='members-detail'),
    path('export_member/', member_views.export_member, name='export-member'),
    path('member_allow/', member_views.member_allow, name='member-allow'),
    path('member_allow_pdf/', member_views.member_allow_pdf, name='member-allow-pdf'),
    path('member_pdf/', member_views.member_pdf, name='member-pdf'),
    path('member_pdf_card/<int:pk>/', member_views.member_pdf_card, name='member-pdf-card'),




    # point urls
    path('point_list/', member_views.point_list, name='point-list'),
    path('point_create/', member_views.point_create, name='point-create'),
    path('point_update/<int:pk>/', member_views.point_update, name='point-update'),
    path('point_delete/<int:pk>/', member_views.point_delete, name='point-delete'),
    path('export_point/', member_views.export_point, name='export-point'),
    path('export_member_allow/', member_views.export_member_allow, name='export-member-allow'),
    path('point_pdf/', member_views.point_pdf, name='point-pdf'),



    # book type urls
    path('booktype_list/', booktype_views.booktype_list, name='booktype-list'),
    path('booktype_create/', booktype_views.booktype_create, name='booktype-create'),
    path('booktype_update/<int:pk>/', booktype_views.booktype_update, name='booktype-update'),
    path('booktype_delete/<int:pk>/', booktype_views.booktype_delete, name='booktype-delete'),
    path('export_booktype/', booktype_views.export_booktype, name='export-booktype'),
    # path('booktype_pdf_view/', BookTypePDFView.as_view(), name='booktype-pdf-view'),
    path('booktype_pdf/', booktype_views.booktype_pdf, name='booktype-pdf'),


    # book urls
    path('book_list', booktype_views.book_list, name='book-list'),
    path('select_book_borrow', booktype_views.select_book_borrow, name='select-book-borrow'),
    path('book_create/', booktype_views.book_create, name='book-create-edit'),
    path('book_update/<int:pk>/', booktype_views.book_update, name='book-update'),
    path('book_delete/<int:pk>/', booktype_views.book_delete, name='book-delete'),
    path('book_detail/<int:pk>/', booktype_views.book_detail, name='book-detail'),
    path('export_book/', booktype_views.export_book, name='export-book'),
    path('book_pdf', booktype_views.book_pdf, name='book-pdf'),
    # path('book_create/', booktype_views.abc, name='abc'),
    path('return_borrow_stauts', booktype_views.return_borrow_stauts, name='return-borrow-stauts'),


    path('return_status_update/<int:pk>/', booktype_views.return_status_update, name='return-status-update'),
    path('book_update_borrow/<int:pk>/', booktype_views.book_update_borrow, name='book-update-borrow'),


    # book store url
    path('bookstore_list', booktype_views.bookstore_list, name='bookstore-list'),
    path('bookstore_create/', booktype_views.bookstore_create, name='bookstore-create'),
    path('bookstore_update/<int:pk>/', booktype_views.bookstore_update, name='bookstore-update'),
    path('bookstore_delete/<int:pk>/', booktype_views.bookstore_delete, name='bookstore-delete'),
    path('export_bookstore/', booktype_views.export_bookstore, name='export-bookstore'),
    # path('bookstore_pdf_view/', BookStorePDFView.as_view(), name='bookstore-pdf-view'),
    path('bookstore_pdf', booktype_views.bookstore_pdf, name='bookstore-pdf'),


    # book order url
    # path('some_view/', booktype_views.some_view, name='some-view'),


    path('order_list/', bookorder_views.order_list, name='order-list'),
    path('order_create/', bookorder_views.order_create, name='order-create'),
    path('order_update/<int:pk>/', bookorder_views.order_update, name='order-update'),
    path('order_delete/<int:pk>/', bookorder_views.order_delete, name='order-delete'),
    path('bookorder_bill_pdf/<int:pk>/', bookorder_views.bookorder_bill_pdf, name='bookorder-bill-pdf'),
    path('export_bookorder/', bookorder_views.export_bookorder, name='export-bookorder'),
    # path('bookorder_pdf_view/', BookOrderPDFView.as_view(), name='bookorder-pdf-view'),

    path('order_pdf/', bookorder_views.order_pdf, name='order-pdf'),


    # path('member_register/', member_views.member_register, name='member-register'),
    path('thanks/', member_views.thanks, name='thanks'),


    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('user_list/', user_views.user_list, name='user-list'),
    path('export_employee/', user_views.export_employee, name='export-employee'),
    path('employee_pdf/', user_views.employee_pdf, name='employee-pdf'),


    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


