# @copyright &copy; 2010 - 2017, Fraunhofer-Gesellschaft zur Foerderung der angewandten Forschung e.V. All rights reserved.
#
# BSD 3-Clause License
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
# 1.  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 2.  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 3.  Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# We kindly request you to use one or more of the following phrases to refer to foxBMS in your hardware, software, documentation or advertising materials:
#
# &Prime;This product uses parts of foxBMS&reg;&Prime;
#
# &Prime;This product includes parts of foxBMS&reg;&Prime;
#
# &Prime;This product is derived from foxBMS&reg;&Prime;

"""WAF script for building "foxbms-stmhal" library.
location of this wscript:
    /src/os/wscript

library output:
    /build/src/os/libfoxbms-os.a

"""

from waflib import Logs, Utils, Context
import os


def build(bld):
    if bld.options.primary:
        bld_project = os.path.normpath('foxBMS-primary')
    elif bld.options.secondary:
        bld_project = os.path.normpath('foxBMS-secondary')
    else:
        print "No valid sources to build"
        sys.exit()
    srcs = ' '.join([
            os.path.join('Source', 'CMSIS_RTOS', 'cmsis_os.c'),
            os.path.join('Source', 'croutine.c'),
            os.path.join('Source', 'list.c'),
            os.path.join('Source', 'portable', 'GCC', 'ARM_CM4F', 'port.c'),
            os.path.join('Source', 'portable', 'MemMang', 'heap_4.c'),
            os.path.join('Source', 'queue.c'),
            os.path.join('Source', 'tasks.c'),
            os.path.join('Source', 'timers.c'),
           ])
    if bld.options.primary:
        temp = 'primary'
    if bld.options.secondary:
        temp = 'secondary'
    srcs += ' ' + os.path.join('..', bld_project, 'src', 'os', 'os.c')

    includes = os.path.join(bld.bldnode.abspath())
    includes += ' '.join([
            '.',

            os.path.join('..', bld_project, 'src', 'application', 'config'),
            os.path.join('..', bld_project, 'src', 'application', 'sox'),
            os.path.join('..', bld_project, 'src', 'application', 'task'),

            os.path.join('..', bld_project, 'src', 'engine', 'config'),
            os.path.join('..', bld_project, 'src', 'engine', 'database'),
            os.path.join('..', bld_project, 'src', 'engine', 'diag'),
            os.path.join('..', bld_project, 'src', 'engine', 'sysctrl'),
            os.path.join('..', bld_project, 'src', 'engine', 'task'),

            os.path.join('..', bld_project, 'src', 'general'),
            os.path.join('..', bld_project, 'src', 'general', 'config'),
            os.path.join('..', bld_project, 'src', 'general', 'includes'),

            os.path.join(bld.top_dir, 'hal', 'CMSIS', 'Device', 'ST', 'STM32F4xx', 'Include'),
            os.path.join(bld.top_dir, 'hal', 'CMSIS', 'Include'),
            os.path.join(bld.top_dir, 'hal', 'STM32F4xx_HAL_Driver', 'Inc'),
            os.path.join(bld.top_dir, 'hal', 'STM32F4xx_HAL_Driver', 'Inc', 'Legacy'),

            os.path.join('..', bld_project, 'src', 'module', 'can'),
            os.path.join('..', bld_project, 'src', 'module', 'cansignal'),
            os.path.join('..', bld_project, 'src', 'module', 'config'),
            os.path.join('..', bld_project, 'src', 'module', 'contactor'),
            os.path.join('..', bld_project, 'src', 'module', 'nvram'),
            os.path.join('..', bld_project, 'src', 'module', 'io'),
            os.path.join('..', bld_project, 'src', 'module', 'mcu'),
            os.path.join('..', bld_project, 'src', 'module', 'rtc'),
            os.path.join('..', bld_project, 'src', 'module', 'utils'),

            os.path.join('..', bld_project, 'src', 'os'),

            os.path.join('Source'),
            os.path.join('Source', 'CMSIS_RTOS'),
            os.path.join('Source', 'include'),
            os.path.join('Source', 'portable', 'GCC', 'ARM_CM4F'),
            ])

    bld.stlib(
              target='foxbms-os',
              source=srcs,
              includes=includes
              )

# vim: set ft=python :
