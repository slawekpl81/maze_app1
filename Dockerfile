# Dockerfile: Fedora + Python + raylib (+ pyray)
FROM fedora:latest

# Aktualizacja systemu i instalacja zależności
RUN dnf update -y && \
    dnf install -y \
        python3 \
        python3-pip \
        python3-devel \
        vim \
        gcc \
        gcc-c++ \
        make \
        cmake \
        git \
        mesa-libGL \
        mesa-libGL-devel \
        libX11-devel \
        libXrandr-devel \
        libXinerama-devel \
        libXcursor-devel \
        libXi-devel \
        alsa-lib-devel \
        pulseaudio-libs-devel \
        openssl-devel \
    && dnf clean all -y

# Klonujemy i kompilujemy raylib (najnowsza wersja z GitHub)
#WORKDIR /opt
# RUN  git clone https://github.com/raysan5/raylib.git raylib && \
#    cd raylib && \
#    mkdir build && cd build && \
#    cmake .. -DCMAKE_BUILD_TYPE=Release && \
#    make -j$(nproc) && \
#    make install

# Instalujemy oficjalne bindingi Pythona dla raylib (pyray)
# Najlepsze i najaktywniejsze obecnie: https://github.com/electronstudio/raylib_python_cffi
RUN pip3 install --no-cache-dir raylib

# Alternatywnie możesz użyć innego bindera, np.:
# RUN pip3 install --no-cache-dir pyraylib
# RUN pip3 install --no-cache-dir pyray

# Ustawiamy katalog roboczy dla Twojej aplikacji
WORKDIR /app

# Kopiujemy (opcjonalnie) Twój kod – odkomentuj jeśli budujesz obraz z kodem
# COPY . .

# Domyślne polecenie – uruchamia powłokę, żebyś mógł testować interaktywnie
#CMD ["python3"]

# Jeśli chcesz od razu uruchamiać konkretną grę:
# CMD ["python3", "main.py"]