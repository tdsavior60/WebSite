import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

'''
# text格式邮件
os.environ['DJANGO_SETTINGS_MODULE'] = 'WebSite.settings'

# send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),
# 失败静默(若发送失败，报错提示我们)

if __name__ == '__main__':

    send_mail(
        '来自maomao60的邮件',
        '欢迎访问我的网站，本站专注于Python内容的分享！',
        'maomao60.wang@hotmail.com',
        [email],
    )
'''
# HTML格式邮件
os.environ['DJANGO_SETTINGS_MODULE'] = 'WebSite.settings'

if __name__ == '__main__':
    # 邮件标题、发件人、收件人
    subject, from_email, to = '来自清风居邮件', 'maomao60.wang@hotmail.com', 'email'
    html_content = '<p>欢迎注册访问<a href="http://{}/confirm/?code={}" target=blank>清风居</a>\
                    <p>本站专注于Python和Django技术的分享！</p>'
    # [to]为收件人列表
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()