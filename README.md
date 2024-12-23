

# glumbOS rice dotfiles

## Gallery
![2024-12-22-131429-hyprshot.png](https://github.com/grinheckerdev/glumbos-dotfiles/blob/main/gallery/2024-12-22-131429_hyprshot.png?raw=true)**Rofi app launcher demo**

![2024-12-22-131321-hyprshot.png](https://github.com/grinheckerdev/glumbos-dotfiles/blob/main/gallery/2024-12-22-131321_hyprshot.png?raw=true)**Power menu**

![2024-12-22-131312-hyprshot.png](https://github.com/grinheckerdev/glumbos-dotfiles/blob/main/gallery/2024-12-22-131312_hyprshot.png?raw=true)**Window tiling**

![2024-12-22-131217-hyprshot.png](https://github.com/grinheckerdev/glumbos-dotfiles/blob/main/gallery/2024-12-22-131217_hyprshot.png?raw=true)
**Listening to glumbo music without tiling the windows**
*Wow! GlumboCoin is up by 900%!!*

![2024-12-22-131019-hyprshot.png](https://raw.githubusercontent.com/grinheckerdev/glumbos-dotfiles/refs/heads/main/gallery/2024-12-22-131019_hyprshot.png)**Glumbo forums**

---
## Why?
This rice should look weird and be silly. It was a free comission for [GlumboCorp ](https://discord.gg/6s7eZy3QPw "https://discord.gg/6s7eZy3QPw"). This is my first rice, please don't judge too much.
# Rice details
## Important
**This was only tested on Asahi Linux Fedora Remix 41 on a MacBook Air M2** if you encounter any issues please report them in the issues tab.

## Config:
 - **WM**: [Hyprland](https://wiki.hyprland.org/Getting-Started/Installation/)
 - **App launcher**: [rofi](https://github.com/davatorium/rofi/blob/next/INSTALL.md)
 - **Terminal**: [alacritty](https://github.com/alacritty/alacritty/blob/master/INSTALL.md)
 - **Bar**: [waybar](https://github.com/Alexays/Waybar)
 - **Screenshot tool**: [Hyprshot](https://github.com/Gustash/Hyprshot)
 - **App shortcuts and waybar tools**: Custom modules (modified ml4w)
 -  **Glumbocoin widget**: custom gtk application (included in the dotfiles)
 - **Power menu**: custom gtk application (included in the dotfiles)
 - **Wallpaper**: I made it myself. [Download link](https://github.com/grinheckerdev/glumbos-dotfiles/blob/main/.config/ml4w/wallpapers/glumbo_wallpaper.png?raw=true)
 - **Fonts**: Can't tell which are default and which aren't, so here are all of the [installed font families](https://raw.githubusercontent.com/grinheckerdev/glumbos-dotfiles/refs/heads/main/fonts_families.txt)
 - **Code editor**: Sublime text (arch installation, check [Additional installation section](https://github.com/grinheckerdev/glumbos-dotfiles?tab=readme-ov-file#additional-installation))
 - **MacOS keybinds**: [Toshy](https://github.com/RedBearAK/toshy) (check [Additional installation section](https://github.com/grinheckerdev/glumbos-dotfiles?tab=readme-ov-file#additional-installation))
 - **Icon font**: [FontAwesome6 Free](https://packages.fedoraproject.org/pkgs/fontawesome-fonts/fontawesome-6-free-fonts/), [FontAweosme6 brands](https://packages.fedoraproject.org/pkgs/fontawesome-fonts/fontawesome-6-brands-fonts/) and a custom font (for glumbocoin and sublime text)
 - **Audio visualizer** [CAVA](https://github.com/karlstav/cava?tab=readme-ov-file#installing)

## Installation
1) **Install all above packages for your system.**
2) **Follow these steps:**

Install Python 3.13 and all needed packages:
**Fedora**
```bash
sudo dnf update -y
sudo dnf install -y python3.13 python3.13-pip
sudo dnf install -y python3-gobject python3-cairo gtk3 pango
```
**Ubuntu/Debian or other os with apt**
(untested instructions, hope they work)
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.13 python3.13-venv python3-pip
sudo apt install -y python3-gi python3-cairo gir1.2-gtk-3.0 gir1.2-pango-1.0
```

Clone the repo:
```bash
git clone https://github.com/grinheckerdev/glumbos-dotfiles
cd glumbos-dotfiles
```
 Copy all files:
```bash
cp -r ./.config/hypr ~/.config
cp -r ./.config/waybar ~/.config
cp -r ./.config/alacritty ~/.config/
cp -r ./.config/ml4w ~/.config/
cp ./fonts/sublime-custom.ttf /usr/share/fonts
sudo fc-cache -v
```

Give permission to run files:
```bash
sudo chmod +x ~/.config/hypr/toggle_glumbocoin.sh
sudo chmod +x ~/.config/ml4w/scripts/keybindings.sh
sudo chmod +x ~/.config/ml4w/scripts/reload-hyprpaper.sh
sudo chmod +x ~/.config/ml4w/scripts/reload-waybar.sh
sudo chmod +x ~/.config/ml4w/settings/browser.sh
sudo chmod +x ~/.config/ml4w/settings/filemanager.sh
sudo chmod +x ~/.config/ml4w/settings/shuffle_colors.sh
sudo chmod +x ~/.config/waybar/shuffle_colors.sh
```

And then reboot or restart hyprland.

## Additional installation / customization

### Installing Sublime Text
For x86 use [these instructions](https://www.sublimetext.com/docs/linux_repositories.html)
For ARM:
```bash
curl --output ./sublime_text.tar.xz "https://download.sublimetext.com/sublime_text_build_4189_arm64.tar.xz"
tar -xvf ./sublime_text.tar.xz
cp -r ./sublime_text /opt
sudo cp /opt/sublime_merge/sublime_merge.desktop /usr/share/applications/
```

Add sublime text icon to the top bar:
```bash
cp -r ./.config.additional/ml4w ~/.config/
```

### Remapping caps to be your mod key (remapping it to super)
```bash
cp -r ./.config.additional/hypr ~/.config/
```
