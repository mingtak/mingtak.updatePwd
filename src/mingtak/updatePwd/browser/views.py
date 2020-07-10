from mingtak.updatePwd import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.interface import Interface
#from plone.directives import form
from plone.autoform import directives as form
#from plone.autoform.form import AutoExtensibleForm
from plone.supermodel import model
from zope import schema
from z3c.form import button
from Products.statusmessages.interfaces import IStatusMessage


class IUpdatePasswordSelf(model.Schema):

    newPassword = schema.TextLine(
        title=_(u"New Password"),
    )

class UpdatePwd:

    def updatePwd(self, id, newPwd):

class UpdatePasswordSelf(BrowserView, UpdatePwd):

    template = ViewPageTemplateFile('templates/update_password_self.pt')

    def __call__(self):

        request = self.request
        if 'newPassword' in request.form:
            user = api.user.get_current()
            id = user.id
            try:
                self.updatePwd(id, newPwd)
                api.portal.show_message('已更新密碼', request,)
            except:
                api.portal.show_message('更新失敗，請聯絡系統管理員', request, 'error')

        return self.template()


class IUpdatePassword(model.Schema):

    accountId = schema.TextLine(
        title=_(u"Account Id"),
    )

    newPassword = schema.TextLine(
        title=_(u"New Password"),
    )


class UpdatePassword(BrowserView, UpdatePwd):

    template = ViewPageTemplateFile('templates/update_password_self.pt')

    def __call__(self):

        request = self.request

        if 'accountId' in request.form:
            id = request.form.get('accountId')
            newPwd = request.form.get('newPassword')
            try:
                self.updatePwd(id, newPwd)
                api.portal.show_message('已更新密碼', request,)
            except:
                api.portal.show_message('更新失敗，請確認帳號正確性，或聯絡系統管理員', request, 'error')

        return self.template()
