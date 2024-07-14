# TD Checker | TSETMC & DDN Checker | برای تمامی صندوق های سرمایه گذاری

## توجه برای استفاده از برنامه حتما ابتدا فایل DDN خود را با دستور زیر وارد کنید

```python
DDn.DDn_F(Ddn_file='محل ادرس دهی DDn')
```

## برای استفاده از پکیج اگر صندوق شما رایان است لطفا از دستور زیر فایل را بهش ارئه دهید(ققط فیکس ها برای استفاده از قیمت پایانی سهام ها)
## باقی نوع صندوق ها طی اپدیت بعدی ارائه میشود

```python
Rayan.Rayan_F(Rayan_file='محل ادرس دهی فایل قیمت کارشناسی صندوق')
```

## برای استفاده از پکیج اگر صندوق شما تدبیر است لطفا از دستور زیر فایل را بهش ارئه دهید

```python
Tadbir.tadbir_F(Tadbir_file='محل ادرس دهی تعدیل قیمت صندوق های تدبیر')
```

## سپس با قرار دادن دستور زیر در اخرین خط فایل پایتونی خود را ران کنید.

```python
RequestsToTse.requests()
```