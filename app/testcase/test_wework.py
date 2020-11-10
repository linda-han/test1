from app.page.app import App


class Test_Wework():

    def test_wework(self):
        self.app = App()
        invitepage = self.app.start().main().goto_memberlist().goto_add_member().goto_manual_addmember().input_name().input_gender().input_phonenumber().save()
        assert  "成功" in invitepage.get_toast()