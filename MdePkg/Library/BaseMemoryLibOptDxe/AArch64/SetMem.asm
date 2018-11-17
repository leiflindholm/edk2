;------------------------------------------------------------------------------
;
; Copyright (c) 2016, Linaro Ltd. All rights reserved.<BR>
;
; This program and the accompanying materials are licensed and made available
; under the terms and conditions of the BSD License which accompanies this
; distribution.  The full text of the license may be found at
; http://opensource.org/licenses/bsd-license.php
;
; THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
; WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
;
;------------------------------------------------------------------------------

    EXPORT  InternalMemZeroMem
    EXPORT  InternalMemSetMem
    EXPORT  InternalMemSetMem16
    EXPORT  InternalMemSetMem32
    EXPORT  InternalMemSetMem64

    AREA    SetMem, CODE, READONLY, CODEALIGN, ALIGN=5

InternalMemZeroMem
InternalMemSetMem
InternalMemSetMem16
InternalMemSetMem32
InternalMemSetMem64
	ret

	END