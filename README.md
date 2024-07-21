<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ChronicleDevs/hence">
    <img src="https://i.postimg.cc/fWFSvCxQ/Hence-1-removebg-preview.png" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">Syndex - SyndexCube</h3>

  <p align="center">
    A simple encryption. Try using it!<br>
    <italic>Note: this program still is part of Hence Group</italic>
    <br />
    <a href="https://github.com/ChronicleDevs/syndexcube"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ChronicleDevs/syndexcube">View Demo</a>
    ·
    <a href="https://github.com/ChronicleDevs/syndexcube/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/ChronicleDevs/syndexcube/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great Encryption in the world such as AES or RSA; But, I am inspired to create one. So, here it is, SyndexCube.

How does SyndexCube works:
* SC works with splitting every data into single character then place it into a big cube-like container (3D array) with different position for each data
* SC isn't provenly strong. and it is not effective when it is used for big data, because SC saved all the splitted data coordinates into one long IV.
* It is just simple project of me, and i am still learning Python. :smile:

Big thanks for who read this, Hence will be evolving to Fence (soon). Fence provides more complex and secure way, but still based on Fernet :smile:. Thanks to all the people have contributed


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

SyndexCube fully built with Python and no other languages included. 

* [![Python][Python]][Python-url]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Instruction how to install and use Hence for your own. Hence includes a Wrapper to make things easier for file encrypting.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip3 install -r requirements.txt
  ```

### Installation

_Install the SC Encryptor. Please make sure you keep following the guide._

1. Make sure you have installed python3 and python3-pip (apt guide)
   ```sh
   sudo apt install python3 python3-pip
   ```
3. Clone the repo
   ```sh
   git clone https://github.com/ChronicleDevs/syndexcube
   ```
4. Install the requirements
   ```sh
   pip3 install -r requirements.txt
   ```
5. Run installation process
   ```python3
   python3 install.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Using Hence in shell (Messages)
   
    - Encrypting messages
      
     ```sh
     hence "Hello, World"
     ``` 
    - Decrypt Messages
      
     ```sh
     hence -d "{encryptedmessages}" -p "{hencekey}"
     ```
2. Using Hence in shell (File)

   - Encrypting file

   ```sh
   hencewrapper file.txt -o file.enc
   ```

   - Decrypt file
  
   ```sh
   hencewrapper -d file.enc -o output.txt -k {HenceKey}
   `

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add File wrapper
- [x] Add ByteHence (for encrypting binary file)
- [ ] Add Fence

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ChronicleDevs/hence.svg?style=for-the-badge
[contributors-url]: https://github.com/ChronicleDevs/hence/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ChronicleDevs/hence.svg?style=for-the-badge
[forks-url]: https://github.com/ChronicleDevs/hence/network/members
[stars-shield]: https://img.shields.io/github/stars/ChronicleDevs/hence.svg?style=for-the-badge
[stars-url]: https://github.com/ChronicleDevs/hence/stargazers
[issues-shield]: https://img.shields.io/github/issues/ChronicleDevs/hence.svg?style=for-the-badge
[issues-url]: https://github.com/ChronicleDevs/hence/issues
[license-shield]: https://img.shields.io/github/license/ChronicleDevs/hence.svg?style=for-the-badge
[license-url]: https://github.com/ChronicleDevs/hence/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=ffffff
[Python-url]: https://www.python.org
