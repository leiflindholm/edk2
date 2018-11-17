	EXPORT ArmIsArchTimerImplemented
	EXPORT AArch64AllDataCachesOperation
	EXPORT ArmDataMemoryBarrier
	EXPORT ArmDataSynchronizationBarrier
	EXPORT ArmInstructionSynchronizationBarrier
	EXPORT ArmReadMpidr
	EXPORT ArmDisableInterrupts
	EXPORT ArmCleanDataCacheEntryBySetWay
	EXPORT ArmDataSynchronizationBarrier
	EXPORT ArmGetInterruptState
	EXPORT ArmCleanInvalidateDataCacheEntryBySetWay
	EXPORT ArmEnableInterrupts
	EXPORT ArmInvalidateInstructionCacheEntryToPoUByMVA
	EXPORT ArmCleanInvalidateDataCacheEntryByMVA
	EXPORT ArmInvalidateDataCacheEntryByMVA
	EXPORT ArmCleanDataCacheEntryToPoUByMVA
	EXPORT ArmCleanDataCacheEntryByMVA
	EXPORT ArmInvalidateDataCacheEntryBySetWay
	EXPORT ArmReadAuxCr
	EXPORT ArmCacheInfo
	EXPORT ArmWriteCpuActlr
	EXPORT ArmReadCpuActlr
	EXPORT ArmWriteAuxCr
	EXPORT ArmReadCntvCt
	EXPORT ArmWriteCntvCval
	EXPORT ArmReadCntvCtl
	EXPORT ArmReadCntvTval
	EXPORT ArmReadCntvCval
	EXPORT ArmWriteCntvCtl
	EXPORT ArmWriteCntvTval
	EXPORT ArmWriteCntFrq
	EXPORT ArmReadCntFrq

	EXPORT ArmDisableInstructionCache
	EXPORT ArmInvalidateInstructionCache
	EXPORT ArmEnableInstructionCache
	EXPORT ArmEnableStackAlignmentCheck
	EXPORT ArmMmuEnabled
	EXPORT ArmSetTTBR0
	EXPORT ArmEnableDataCache
	EXPORT ArmReadCurrentEL
	EXPORT ArmReplaceLiveTranslationEntry
	EXPORT ArmSetTCR
	EXPORT ArmSetMAIR
	EXPORT ArmGetTCR
	EXPORT ArmEnableMmu
	EXPORT ArmInvalidateTlb
	EXPORT ArmDisableAlignmentCheck
	EXPORT ArmDisableMmu
	EXPORT ArmGetTTBR0BaseAddress
	EXPORT ArmDisableDataCache
	EXPORT ArmReplaceLiveTranslationEntrySize
	EXPORT ArmReadHcr
	EXPORT RegisterEl0Stack
	EXPORT ArmWriteHcr
	EXPORT ArmWriteVBar
	EXPORT ExceptionHandlersStart
	EXPORT ExceptionHandlersEnd
	EXPORT ArmEnableAsynchronousAbort
	EXPORT ArmEnableFiq
	EXPORT ArmDisableFiq
	EXPORT ArmGetFiqState
	EXPORT ArmIsMpCore

	EXPORT ArmWriteTpidrurw
	EXPORT ArmReadTpidrurw
	EXPORT ArmEnableBranchPrediction
	EXPORT ArmGetPhysAddrTop
	EXPORT ArmPlatformIsPrimaryCore

	EXPORT SecSwitchStack
	EXPORT PeiVectorTable
	AREA VSDummy, CODE, READONLY

ArmIsArchTimerImplemented
AArch64AllDataCachesOperation
ArmDataMemoryBarrier
ArmDataSynchronizationBarrier
ArmInstructionSynchronizationBarrier
ArmReadMpidr
ArmDisableInterrupts
ArmCleanDataCacheEntryBySetWay
ArmGetInterruptState
ArmCleanInvalidateDataCacheEntryBySetWay
ArmEnableInterrupts
ArmInvalidateInstructionCacheEntryToPoUByMVA
ArmCleanInvalidateDataCacheEntryByMVA
ArmInvalidateDataCacheEntryByMVA
ArmCleanDataCacheEntryToPoUByMVA
ArmCleanDataCacheEntryByMVA
ArmInvalidateDataCacheEntryBySetWay
ArmReadAuxCr
ArmCacheInfo
ArmWriteCpuActlr
ArmReadCpuActlr
ArmWriteAuxCr

ArmReadCntvCt
ArmWriteCntvCval
ArmReadCntvCtl
ArmReadCntvTval
ArmReadCntvCval
ArmWriteCntvCtl
ArmWriteCntvTval
ArmWriteCntFrq
ArmReadCntFrq

ArmDisableInstructionCache
ArmInvalidateInstructionCache
ArmEnableInstructionCache
ArmEnableStackAlignmentCheck
ArmMmuEnabled
ArmSetTTBR0
ArmEnableDataCache
ArmReadCurrentEL
ArmReplaceLiveTranslationEntry
ArmSetTCR
ArmSetMAIR
ArmGetTCR
ArmEnableMmu
ArmInvalidateTlb
ArmDisableAlignmentCheck
ArmDisableMmu
ArmGetTTBR0BaseAddress
ArmDisableDataCache
ArmReplaceLiveTranslationEntrySize
ArmReadHcr
RegisterEl0Stack
ArmWriteHcr
ArmWriteVBar
ExceptionHandlersStart
ExceptionHandlersEnd
ArmEnableAsynchronousAbort
ArmEnableFiq
ArmDisableFiq
ArmGetFiqState
ArmIsMpCore

ArmWriteTpidrurw
ArmReadTpidrurw
ArmEnableBranchPrediction
ArmGetPhysAddrTop
ArmPlatformIsPrimaryCore

SecSwitchStack
PeiVectorTable
	ret

	END