mail_lib
======================
���[���Ɋ֘A���郉�C�u�������쐬���܂����B
�����p�͎��ȐӔC�ł����R�ɂǂ���

�g����
------
�P�Dpip�R�}���h�����s���A���W���[�����_�E�����[�h���Ă�������

    pip install mail_lib

�Q�D�N���X���C���|�[�g���A���L��̗p�Ɏg�p���Ă�������

    from mail_lib.mail_utils import send_mail
    send_mail(['hoge@mail.com', 'huga@mail.com'], 'title', 'message\nmessage2', 'no-reply@mail.com', '192.168.1.1' )


�@�\�Љ�
------
### ���[�e�B���e�B
#### ���[���֘A
***
send_mail(to_addr_list, subject, message, from_addr, smtp_host, smtp_port=25, cc_addr_list=[], bcc_addr_list=[]):���[���𑗐M���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| to_addr_list | �� | ���M�惁�[���A�h���X | - | 
| subject | �� | ���� | - |
| message | �� | ���b�Z�[�W�A���s�R�[�h�ŋ�؂�΁A���[�����e�����s����܂� | - |
| from_addr | �� | ���M�����[���A�h���X | - |
| smtp_host | �� | smtp�T�[�o�h���C�� | - |
| smtp_port | �~ | smtp�T�[�o�|�[�g | 25 |
| cc_addr_list | �~ | CC���[���A�h���X | [] |
| bcc_addr_list | �~ | BCC���[���A�h���X | [] |
�߂�l�F�Ȃ�
***
send_attach_file_mail(to_addr_list, subject, message, file_path, from_addr, smtp_host, smtp_port=25, cc_addr_list=[], bcc_addr_list=[]):�t�@�C����Y�t�������[���𑗐M���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| to_addr_list | �� | ���M�惁�[���A�h���X | - | 
| subject | �� | ���� | - |
| message | �� | ���b�Z�[�W�A���s�R�[�h�ŋ�؂�΁A���[�����e�����s����܂� | - |
| file_path | �� | �Y�t����t�@�C���̃p�X | - |
| from_addr | �� | ���M�����[���A�h���X | - |
| smtp_host | �� | smtp�T�[�o�h���C�� | - |
| smtp_port | �~ | smtp�T�[�o�|�[�g | 25 |
| cc_addr_list | �~ | CC���[���A�h���X | [] |
| bcc_addr_list | �~ | BCC���[���A�h���X | [] |
�߂�l�F�Ȃ�
***


�֘A���
--------
1. [�O�O���J�X(�u���O)](http://gugurekasu.blogspot.jp/)
2. [LinkedIn](https://jp.linkedin.com/in/akirataniguchi1)
 
���C�Z���X
----------
Distributed under the [MIT License][mit].
[MIT]: http://www.opensource.org/licenses/mit-license.php
