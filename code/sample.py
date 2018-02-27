# -*- coding: utf-8 -*-

def detectAtMe(MyName, content):
  return '@' + MyName in content

def onQQMessage(bot, contact, member, content):
  MyName = '周知'
  if content == '--stop_by_chuck':
    bot.SendTo(contact, 'QQ机器人已关闭')
    bot.Stop()
  elif detectAtMe(MyName, content) and member != None:
    from tf import dataManage
    StatusCode, respond = dataManage(MyName, content, member.qq)
    if StatusCode < 0 and respond:
      bot.SendTo(contact, respond)
    # logging