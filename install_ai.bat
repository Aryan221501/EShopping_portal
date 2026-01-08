@echo off
echo ========================================
echo Installing AI Dependencies
echo ========================================
echo.
echo This will install:
echo - PyTorch (Deep Learning)
echo - Transformers (Hugging Face)
echo - Sentence Transformers (Embeddings)
echo - Scikit-learn (ML algorithms)
echo.
echo This may take 5-10 minutes...
echo.

pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers
pip install sentence-transformers
pip install scikit-learn
pip install numpy

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo You can now use:
echo - AI Chatbot at /chatbot/
echo - Advanced Recommendations
echo - Trending Products at /trending/
echo.
pause
