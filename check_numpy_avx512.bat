@rem Disable NumPy dispatching to AVX512_SKX feature extensions if the chip is
@rem reported to support the feature and NumPy >= 1.22 as this results in the use
@rem of low accuracy SVML libm replacements in ufunc loops.

for /f %%i in (^
'python -c "from numba.misc import numba_sysinfo; ^
sysinfo=numba_sysinfo.get_sysinfo(); ^
print(sysinfo[\"NumPy AVX512_SKX detected\"] and sysinfo[\"NumPy Version\"]>=\"1.22\")"'^
) do set NUMPY_DETECTS_AVX512_SKX_NP_GT_122=%%i

echo NumPy ^>= 1.22 with AVX512_SKX detected: %NUMPY_DETECTS_AVX512_SKX_NP_GT_122%

if "%NUMPY_DETECTS_AVX512_SKX_NP_GT_122%"=="True" (
    set NPY_DISABLE_CPU_FEATURES=AVX512_SKX
)
