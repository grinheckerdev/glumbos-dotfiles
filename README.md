
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
This rice should look weird. It was a free comission for [GlumboCorp ](https://discord.gg/6s7eZy3QPw "https://discord.gg/6s7eZy3QPw"):
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
 - **Wallpaper**: I made it myself. [Download link](https://i.postimg.cc/XqH5fcHh/glumbo-wallpaper.png)
 - **Fonts**: Can't tell which are default and which aren't, so here are all of the [installed font families](https://raw.githubusercontent.com/grinheckerdev/glumbos-dotfiles/refs/heads/main/fonts_families.txt)
 - **Code editor**: Sublime text (arch installation, check [Additional installation section](https://github.com/grinheckerdev/glumbos-dotfiles?tab=readme-ov-file#additional-installation))
 - **MacOS keybinds**: [Toshy](https://github.com/RedBearAK/toshy) (check [Additional installation section](https://github.com/grinheckerdev/glumbos-dotfiles?tab=readme-ov-file#additional-installation))
 - **Icon font**: [FontAwesome6 Free](https://packages.fedoraproject.org/pkgs/fontawesome-fonts/fontawesome-6-free-fonts/), [FontAweosme6 brands](https://packages.fedoraproject.org/pkgs/fontawesome-fonts/fontawesome-6-brands-fonts/) and a custom font (for glumbocoin and sublime text)

## Installation
1) **Install all above packages for your system.**
2) **Follow these steps:**

Install Pyhton 3.13 and all needed packages:
```bash
sudo dnf update -y
sudo dnf install -y python3.13 python3.13-pip
sudo dnf install -y python3-gobject python3-cairo gtk3 pango
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
```

## Additional installation


