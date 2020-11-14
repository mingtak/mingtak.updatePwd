# -*- coding: utf-8 -*-

from mingtak.updatePwd import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
#from zope.interface import Interface
#from plone.directives import form
#from zope import schema
#from z3c.form import button
#from Products.statusmessages.interfaces import IStatusMessage


class UpdatePasswordSelf(BrowserView):
    """ 更新自己密碼 """

    template = ViewPageTemplateFile('templates/update_password_self.pt')

    def __call__(self):

        request = self.request

        if 'submit' in request.form:
            result = self.handleApply()
            if result:
                api.portal.show_message(message=_('密碼更新成功'), request=request)
                return self.template()
            else:
                api.portal.show_message(message=_('密碼更新失敗，請重新輸入'), request=request, type='error')
                return self.template()
        return self.template()


    def handleApply(self):
        request = self.request
        response = request.response
        portal = api.portal.get()

        if api.user.is_anonymous():
            response.redirect(portal.absolute_url())
            return

        newPassword = self.request.form['newPassword']
        newPassword2 = self.request.form['newPassword2']

        import pdb; pdb.set_trace()
        if newPassword != newPassword2 or len(newPassword) <= 5:
            return False

        user = api.user.get_current()
        accountid = user.id
        if user:
            user.setSecurityProfile(password=newPassword)
            return True
        return False


class UpdatePassword(BrowserView):

    template = ViewPageTemplateFile('templates/update_password.pt')

    def __call__(self):

        request = self.request

        if 'submit' in request.form:
            result = self.handleApply()
            if result:
                api.portal.show_message(message=_('密碼更新成功'), request=request)
                return self.template()
            else:
                api.portal.show_message(message=_('密碼更新失敗，請重新輸入'), request=request, type='error')
                return self.template()
        return self.template()


    def handleApply(self):
        request = self.request
        response = request.response
        portal = api.portal.get()

        if api.user.is_anonymous():
            response.redirect(portal.absolute_url())
            return

        accountId = self.request.form['accountId']
        newPassword = self.request.form['newPassword']
        user = api.user.get(username=accountId)
        if user:
            user.setSecurityProfile(password=newPassword)
            message = _(u"Already update password!")
            mType = 'info'
        else:
            message = _(u"User not found!")
            mType = 'warning'

        response.redirect('%s/%s' % (portal.absolute_url(), self.__name__))
        api.portal.show_message(message=message, request=request, type=mType)
        return
