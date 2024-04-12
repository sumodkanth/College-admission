import React from "https://esm.sh/react@18.2.0";
import * as reactIcons from "https://cdn.skypack.dev/react-icons@4.8.0";
import {
  IoIosArrowBack,
  IoIosArrowForward
} from "https://cdn.skypack.dev/react-icons@4.8.0/io";
import { BiSearchAlt2 } from "https://cdn.skypack.dev/react-icons@4.8.0/bi";
import { ImCross } from "https://cdn.skypack.dev/react-icons@4.8.0/im";
import {
  FaHeart,
  FaBars,
  FaPaw,
  FaTwitter,
  FaFacebookF,
  FaLinkedinIn,
  FaYoutube
} from "https://cdn.skypack.dev/react-icons@4.8.0/fa";
import { HiShoppingCart } from "https://cdn.skypack.dev/react-icons@4.8.0/hi";
import {RiInstagramFill} from "https://cdn.skypack.dev/react-icons@4.8.0/ri"
import ReactDOM from "https://esm.sh/react-dom@18.2.0";

const linklst = [
  { id: 1, text: "home" },

  { id: 2, text: "about" },
  { id: 3, text: "services" },
  { id: 4, text: "breeds" },
  { id: 5, text: "shop" },
  { id: 6, text: "gallery" }
];

const slidelst = [
  {
    id: 1,
    url:
      "https://raw.githubusercontent.com/Nis-chal/DogCare-React-/main/dogcare/src/assets/doggroup.png"
  },

  {
    id: 2,
    url:
      "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80"
  },
  {
    id: 3,
    url:
      "https://images.unsplash.com/photo-1615266508040-7c47f7339963?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80"
  },
  {
    id: 4,
    url:
      "https://images.unsplash.com/photo-1581888227599-779811939961?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80"
  }
];

const servicelst = [
  {
    id: 0,
    url: 'https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/service.png?raw=true',

    desc: "We are enhancing our skills, salon, and equipment to meet the challenges of pet grooming.",
    title: "Dog/Cat Grooming",
  },
  {
    id: 1,
    url: 'https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/service2.png?raw=true',
    desc: "Our goal is to ensure pet welfare through home treatment and prompt client response.",
    title: "Home Treatment",
  },
  {
    id: 2,
    url: 'https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/service3.png?raw=true',
    desc: "Our clinic offers professional veterinary care with a focus on disease prevention, diagnosis, and treatment.",
    title: "Clinical Treatment",
  },
  {
    id: 3,
    url: 'https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/service4.png?raw=true',
    desc: "We buy and sell common breed puppies like Golden Retriever, Husky, Pug, etc. 100% guarantee on the breed offered.",
    title: "Puppies Buying & Selling",
  },
  {
    id: 4,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/service5.png?raw=true",
    desc: "Our team of dog trainers is passionate, dedicated, and has years of professional experience.",
    title: "Dog Training",
  },
  {
    id: 5,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/service6.png?raw=true",
    desc: "Quality breeding requires experience and passion. We can arrange and facilitate quality breed mating.",
    title: "Dog Matting",
  },
  ]

const petlst = [
  {
    id: 1,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet.png?raw=true",
    name: "Golden Retriever",
    gender: "Male",
    age: "2 months",
  },
  {
    id: 2,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet1.png?raw=true",
    name: "Doberman",
    gender: "Male",
    age: "2 months",
  },
  {
    id: 3,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet2.png?raw=true",
    name: "Apso",
    gender: "Female",
    age: "1 year",
  },
  {
    id: 4,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet3.png?raw=true",
    name: "Chihuahua",
    gender: "FeMale",
    age: "1 year",
  },
  {
    id: 5,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet4.png?raw=true",
    name: "Japanese Spitz",
    gender: "Male",
    age: "2 months",
  },
  {
    id: 6,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet5.png?raw=true",
    name: "German Shepard",
    gender: "Male",
    age: "2 months",
  },
  {
    id: 7,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet6.png?raw=true",
    name: "Husky",
    gender: "Female",
    age: "3 months",
  },
  {
    id: 8,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/pet7.png?raw=true",
    name: "Pug",
    gender: "Female",
    age: "4 months",
  },

];


const bloglst = [
  {
    id: 1,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/blog1.png?raw=true",
    title: "How to Choose the Right Bully Stick for Your Dog",
    desc: "Below is an excerpt of porch.com article “ Moving with Pets? We have the Experts advice to do it Properly.",
  },
  {
    id: 2,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/blog2.png?raw=true",
    title: "Saving Lives: Animal House Shelter And Downtown Pet Supply",
    desc: "Below is an excerpt of porch.com article “ Moving with Pets? We have the Experts advice to do it Properly.",
  },
  {
    id: 3,
    url: "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/blog3.png?raw=true",
    title: "Himalayan Yak Chews: 11 Benefits You Need To Know",
    desc: "Below is an excerpt of porch.com article “ Moving with Pets? We have the Experts advice to do it Properly.",
  },
];

const SearchInput = ({ show, toggleSearch }) => {
  return (
    <div
      className={
        show
          ? "bg-white  lg:min-w-[250px] md:min-w=[270px]  w-full items-center   lg:w-full  rounded-[25px] border-2 border-[#007fff] align-middle p-[6px] flex-row flex "
          : "bg-white p-0 lg:min-w-[250px] md:min-w=[270px]  w-max lg:w-full item-center rounded-[25px] lg:border-2 lg:border-[#007fff] lg:align-middle lg:p-[6px] lg:flex-row lg:flex "
      }
    >
      <input
        type="search"
        placeholder="Enter to search"
        className={
          show ? " lg-flex rounded-[25px]" : "hidden lg:flex rounded-[25px]"
        }
      />

      <div
        className={
          show
            ? "flex items-center justify-center "
            : "search-icon  bg-[#007fff] rounded-[50px] flex items-center justify-center p-[1px] w-[30px] h-[30px]  "
        }
        onClick={toggleSearch}
      >
        <ImCross
          className={
            show
              ? "flex lg:hidden cursor-pointer "
              : "hidden lg:hidden cursor-pointer"
          }
        />

        <BiSearchAlt2
          className={
            show
              ? "text-white w-[35px] h-[35px] p-[7px] hidden lg:flex cursor-pointer text-[20px] sm:text-[25px] "
              : "text-white cursor-pointer w-[35px] h-[35px] p-[7px]  lg:flex text-[20px] sm:text-[25px] "
          }
        />
      </div>
    </div>
  );
};

const Slider = () => {
  const [active, setActive] = React.useState(0);

  const onNext = () => {
    setActive((prev) => {
      return prev === slidelst.length - 1 ? prev : prev + 1;
    });
  };

  const onPrev = () => {
    setActive((prev) => {
      return prev === 0 ? prev : prev - 1;
    });
  };
  return (
    <div className="slider relative h-[80vh]">
      {slidelst.map((item, index) => (
        <div
          className={
            active != index ? "hidden w-[100%] h-[100%]" : "w-[100%] h-[100%]"
          }
          key={item.id}
        >
          <img src={item.url} alt="" className="h-full w-full object-cover" />
        </div>
      ))}

      <div className="slider-info">
        <h1 className="slider-title heading-color Nunito-font font-[900] text-[30px] lg:text-[40px] ">
          We provide the best care to our furry friends!
        </h1>
        <h5 className="slider-subtitle Nunito-font font-[600]">
          Top Quality of Pet Product Store.
        </h5>
      </div>

      <div
        className={
          active === 0
            ? "slider-icon left cursor-default"
            : "slider-icon left active cursor-pointer"
        }
        onClick={onPrev}
      >
        <IoIosArrowBack />
      </div>

      <div
        onClick={onNext}
        className={
          active === slidelst.length - 1
            ? "slider-icon right cursor-default"
            : "slider-icon right active cursor-pointer"
        }
      >
        <IoIosArrowForward />
      </div>
    </div>
  );
};
const Navbar = () => {
  const [dropdown, setDropDowm] = React.useState(false);
  const [showSearch, setSearch] = React.useState(false);
  const [tab, setTab] = React.useState(1);

  const toggleDoprDown = () => {
    setDropDowm((prev) => !prev);
  };
  const toggleSearch = () => {
    if (window.innerWidth < 1024) setSearch((prev) => !prev);
  };
  return (
    <nav className="relative lg:static min-h-[10vh] px-[2%] sm:px-[5%] ">
      <div
        className={
          showSearch
            ? "hidden lg:flex lg:items-center lg:gap-[2%]   lg:font-[600] lg:text-[30px] cursor-pointer  group "
            : "nav-heading cursor-pointer group text-[clamp(20px,15px_+_4vw,25px)]  lg:text-[30px]"
        }
      >
        <FaPaw className="font-bold paw-icon group-hover:text-[var(--blue-500)]" />
        <h1 className=" whitespace-nowrap Nunito-font font-bold ">Pet Care</h1>
      </div>
      <div
        className={
          dropdown
            ? "flex flex-col gap-[5%] text-center font-[15px] lg:flex-row h-max p-3 lg:p-0 lg:justify-between w-[100%] absolute left-0 bg-white lg:w-[35%]  top-full lg:static bg-blue z-40  "
            : "flex-row gap-[5%] font-[15px] justify-between w-[35%] absolute  bg-white  bottom-full lg:static bg-blue -  hidden lg:flex "
        }
      >
        {linklst.map((item) => {
          return (
            <span
              onClick={() => setTab(item.id)}
              className={
                item.id === tab
                  ? "nav-item active py-3  lg:py-0 hover:text-[#007fff]  hover:lg:bg-transparent hover:bg-[#f5fafa] "
                  : "nav-item  py-3 lg:py-0 hover:text-[#007fff] hover:bg-[#f5fafa]  hover:lg:bg-transparent"
              }
              key={item.id}
            >
              {item.text}
            </span>
          );
        })}
      </div>

      <div
        className={
          showSearch
            ? "d-flex  w-[100%] lg:w-[40%] nav-search  lg:static ms-auto "
            : "d-flex  w-[40%] nav-search  lg:static  ms-auto  justify-end "
        }
      >
        <div
          className={
            showSearch ? "w-[100%] lg:w-[100%]  " : "w-max lg:w-[100%] "
          }
        >
          <SearchInput show={showSearch} toggleSearch={toggleSearch} />
        </div>
        <div className=" nav-options ">
          <FaHeart className="heart-icon text-[20px] sm:text-[25px] text-[var(--blue-500)] cursor-pointer " />
          <div className="nav-cart cursor-pointer relative flex flex-row items-center   xl:pr-[22.15625px] xl:pt-[16px] xl:pb-[17px] xl:pl-[22px] lg:rounded-[8px]  xl:border-[1px] xl:border-[#007fff] xl:border-solid xl:gap-[11.421875px] xl:rounded-[8px]">
            <HiShoppingCart className="text-[20px] sm:text-[25px] text-[var(--blue-500)]" />
            <span className=" xl:after:content-['items'] xl:after:ms-2 xl:static xl:text-[1rem] xl:w-min xl:h-min xl:bg-transparent xl:top-0 absolute top-[-15px] right-[-2px] text-[9px] h-[15px] w-[15px] bg-red-500 flex flex-row items-center justify-center rounded-[50px] text-white xl:text-black  xl:translate-y-0 ">
              2
            </span>
          </div>
        </div>
        <div
          className={
            dropdown
              ? "hamburger lg:hidden flex cursor-pointer  text-[var(--blue-500)] w-[30px] h-[30px] flex-row "
              : "hamburger  lg:hidden cursor-pointer  text-[var(--blue-500)]  w-[30px] h-[30px] flex-row items-center justify-center"
          }
          onClick={toggleDoprDown}
        >
          {dropdown ? (
            <ImCross className="fa-bars text-[20px] sm:text-[25px]" />
          ) : (
            <FaBars className="fa-bars text-[20px] sm:text-[25px]" />
          )}
        </div>
      </div>
    </nav>
  );
};

const Footer = () => {
  return (
    <div className="bg-[#17224D] text-white">
      <div className=" min-h-[40vh] flex flex-col gap-[5%]  lg:flex-row lg:justify-between px-[5%] py-[4%] text-white">
        <div className="flex flex-col gap-[6%] lg:gap-[25%] basis-[50%]   lg;justify-between ">
          <div className="flex flex-row justify-between items-center gap-[5%] lg:gap-0">
            <div className=" ">
              <FaPaw className="text-[5rem] text-white " />
            </div>
            <p className="text-white lg:w-[70%] font-thin ">
              " City Pet House & Animal Clinic: Quality and affordable animal
              care at your doorstep. Comprehensive, professional, and
              compassionate veterinary services by our dedicated and experienced
              team. "
            </p>
          </div>
          <div className="flex flex-row gap-4 md:flex-col lg:gap-5 mt-6 lg:mt-0">
            <div className="flex flex-col">
              <small>Phone Number</small>
              <p className="font-bold ">(555) 555-1234</p>
            </div>
            <div className="flex flex-col">
              <small>location</small>
              <p className="font-bold ">nischalchan@gmail.com</p>
            </div>
          </div>
        </div>
        <div className="flex  flex-col gap-2 mt-6 lg:mt-0">
          <strong className=" ">Menu</strong>
          <div className="flex flex-row flex-wrap lg:flex-col gap-2">
            {linklst.map((item) => {
              return (
                <span key={item.id} className=" ">
                  {item.text}
                </span>
              );
            })}
          </div>
        </div>
        <div className="flex flex-col gap-2 mt-6 lg:mt-0">
          <strong>Gallery</strong>
          <div className="gap-[5%] grid-cols-4 lg:grid-cols-2 grid">
            <img className="" src={"https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/Container.png?raw=true"} alt="" srcSet="" />
            <img className="" src={"https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/Container1.png?raw=true"} alt="" srcSet="" />
            <img className="" src={"https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/Container2.png?raw=true"} alt="" srcSet="" />
            <img className="" src={"https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/Container3.png?raw=true"} alt="" srcSet="" />
          </div>
        </div>
      </div>

      <section className="lg:ps-[5%] px-[5%] lg:pr-0">
        <hr className="text-white" />
        <div className="flex flex-col gap-3 lg:gap-0 lg:flex-row lg:justify-between py-4">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque,
            doloremque!
          </p>
          <div className="flex flex-row gap-3 pr-3">
            <div className="bg-white p-2 text-black rounded-md ">
              <FaFacebookF />
            </div>
            <div className="bg-white p-2 text-black rounded-md ">
              <FaTwitter />
            </div>
            <div className="bg-white p-2 text-black rounded-md ">
              <RiInstagramFill />
            </div>
            <div className="bg-white p-2 text-black rounded-md ">
              <FaLinkedinIn />
            </div>
            <div className="bg-white p-2 text-black rounded-md ">
              <FaYoutube />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

const App = () => {
  return (
    <>
         <section className=" w-100 text-[12px] sm:text-[16px] bg-[#007fff] text-white font-[700] text-center py-3 ">
        Call us for Veterinary Support: (555) 555-1234
      </section>
      <section className="">
        <Navbar />
      </section>
      <section id="one">
        <Slider />
      </section>

      <section
        id="about"
        className="grid grid-cols-1 md:grid-cols-2 box gap-[5%] h-[100vh] "
      >
        <div className="about-img relative lg  hidden md:flex pt-[10%] md:mt-[10%] lg:mt-0 ">
          <div className="absolute top-[10%] right-[13%] aspect-[1/1] w-[60%]   ">
            <img
              src={
                "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/Vector.png?raw=true"
              }
              alt=""
              className=" object-contain w-full h-full "
            />
          </div>
          <div className="absolute md:top-[45%] lg:top-[62%] left-[15%] aspect-[1/1] w-[30%]">
            <img
              src={
                "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/Vector1.png?raw=true"
              }
              alt=""
              className=" object-contain w-full h-full "
            />
          </div>
          <div className="absolute top-[23%] left-0 bg-white p-[1%] rounded-md aspect-[1/1] w-[65%] ">
            <img
              src={
                "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/About1.png?raw=true"
              }
              alt=""
              className="object-cover w-full h-full"
            />
          </div>
          <div className="absolute top-[40%] lg:top-[60%] right-[27%] bg-white p-[1%] rounded-md  aspect-[1.2/1] w-[42%] ">
            <img
              src={
                "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/About3.png?raw=true"
              }
              alt=""
              className="object-cover w-full h-full"
            />
          </div>
          <div className="absolute md:top-[35%] lg:top-[47%] right-[20%] bg-white p-[1%] rounded-md w-[30%]  ">
            <img
              src={
                "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/About2.png?raw=true"
              }
              alt=""
              className=""
            />
          </div>
        </div>

        <div className="about-info pt-[25%] flex flex-col gap-[5%] ">
          <h1 className="Nunito-font font-[800] text-[45px] text-[var(--blue-1000)]  ">
            About us
          </h1>
          <p className="leading-[32px] text-[22px] text-[var(--dark-100)]">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe
            corporis omnis in, delectus fugit numquam incidunt ad consequuntur
            doloribus
          </p>

          <ul className="flex flex-col gap-4">
            <li className="flex flex-row gap-2 items-center">
              <div className="w-[14px] h-[14px]">
                <img
                  src={
                    "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/tick.png?raw=true"
                  }
                  alt=""
                  className="w-full h-full object-contain"
                />
              </div>{" "}
              Comprehensive
            </li>
            <li className="flex flex-row gap-2 items-center">
              <div className="w-[14px] h-[14px]">
                <img
                  src={
                    "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/tick.png?raw=true"
                  }
                  alt=""
                  className="w-full h-full object-contain"
                />
              </div>{" "}
              Professional
            </li>
            <li className="flex flex-row gap-2 items-center">
              <div className="w-[14px] h-[14px]">
                <img
                  src={
                    "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/tick.png?raw=true"
                  }
                  alt=""
                  className="w-full h-full object-contain"
                />
              </div>{" "}
              Comprehensive verterinary service
            </li>
          </ul>

          <button className="flex flex-row p-2 lg:w-[160px] justify-between ps-[5%] w-[calc(140px_+_5%)] text-white gap-3 rounded-[25px]  bg-[var(--blue-500)] items-center">
            Contact{" "}
            <div className="w-[30px] aspect-[1/1] rounded-[50px] bg-white flex flex-row justify-center items-center">
              <IoIosArrowForward className=" text-[var(--blue-500)]" />
            </div>
          </button>
        </div>
      </section>
      
      
      <section className="p-[5%]    flex flex-col gap-7  justify-center ">
        <h1 className="Nunito-font font-[800] text-[45px] text-[var(--blue-1000)] text-center  ">
          Our Services
        </h1>
        <p className="Nunito-font font-[500] text-[clamp(14px_,11px_+_1vw,_22px)] text-center  lg:text-[clamp(14px_,13px_+_5vw,_26px)] md:leading-8  ">
          We provide a wide range of products & services for pets such as food,
          toys, grooming supplies, and veterinary care. We aim to meet the needs
          of pet owners and ensure the health and happiness of their furry
          friends.
        </p>
        <div className="grid  grid-cols-[repeat(2,1fr)] md:grid-cols-3  lg:gap-[5%]   lg:px-[5%] w-full gap-y-[20px] gap-x-[5%] ">
          {servicelst.map((item) => {
            return (
              <div
                className="aspect-[1/1.4] lg:aspect-[1/1.2]  border-[var(--border-color)] border-[1px] border-solid rounded-lg  flex flex-col w-full "
                key={item?.id}
              >
                <div className=" aspect-[1/0.5] w-full">
                  <img
                    src={item?.url}
                    alt=""
                    className="w-full  object-cover"
                  />
                </div>
                <div className="p-[5%]   flex flex-col justify-between flex-1 ">
                  <h2 className="Nunito-font text-[14px] lg:text-[20px] font-[800] text-[var(--blue-1000)] line-clamp-1 ">
                    {item?.title}
                  </h2>
                  <p className="text-[12px] md:text-[16px] Nunito-font font-[500] text-[var(--dark-100)] line-clamp-2 lg:line-clamp-4 ">
                    {item?.desc}
                  </p>
                  <div className="flex flex-row justify-center justify-self-end mt-auto  ">
                    <button className="mx-auto bg-[var(--blue-1000)] text-[14px] text-white sm:rounded-md rounded-sm p-[2%] w-[60%] lg:w-[35%] py-1 sm:py-2  lg:py-3 inter-font font-[500] ">
                      view more
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>
      
      <section
        id="pet-collection"
        className="p-[5%]    flex flex-col gap-7 h-max justify-center "
      >
        <h1 className="Nunito-font font-[800] text-[45px] text-[var(--blue-1000)] text-center  ">
          Our Pet Collections
        </h1>
        <p className="Nunito-font font-[500] text-[clamp(14px_,11px_+_1vw,_22px)] text-center  lg:text-[clamp(14px_,13px_+_5vw,_26px)] md:leading-8  ">
          "Bring joy to your home with a furry companion from our pet
          selection."
        </p>

        <div className="grid grid-cols-[repeat(2,1fr)] grid-rows-[repeat(1,1fr)] md:grid-cols-3 lg:grid-cols-4 gap-y-[20px] gap-x-[5%] ">
          {petlst.map((item) => {
            return (
              <div
                key={item.id}
                className="p-[2%] border-[var(--border-color)] border-solid border-[1px] rounded-md"
              >
                <div className="aspect-[1/1.0.5] rounded-md overflow-hidden">
                  <img
                    src={item.url}
                    alt=""
                    className="w-full h-full object-cover"
                  />
                </div>
                <div className="pet-info my-[5%]">
                  <p className="Nunito-font text-[var(--blue-1000)] font-[800] leading-[24px]  ">
                    {item.name}
                  </p>
                  <div className="flex flex-col sm:flex-row items-start gap-2 sm:items-center ">
                    <p className="Nunito-font font-[400] text-[12px]">
                      Gender : <strong>{item.gender}</strong>
                    </p>
                    <p className="Nunito-font font-[400] text-[12px]">
                      Age : <strong>{item.age}</strong>
                    </p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        <div className="flex flex-row justify-center">
          <button className="flex flex-row p-2 lg:w-[160px] gap-[15%]  justify-center w-[calc(140px_+_5%)] whitespace-nowrap  text-white  rounded-[25px]  bg-[var(--blue-500)] items-center">
            <span className="ms-auto">View All</span>
            <div className="w-[30px] aspect-[1/1] rounded-[50px] bg-white flex flex-row justify-center items-center ">
              <IoIosArrowForward className=" text-[var(--blue-500)]" />
            </div>
          </button>
        </div>
      </section>

      <section className="h-[40vh] overflow-hidden rounded-[20px] bg-black  mx-[2%] relative ">
        <div className="w-full h-full">
          <img
            src={
              "https://github.com/Nis-chal/DogCare-React-/blob/main/dogcare/src/assets/specdog.png?raw=true"
            }
            alt=""
            className="w-full h-full object-cover object-right"
          />
        </div>

        <div className="find-info absolute top-[20%] left-[5%] text-[var(--white-1000)] flex flex-col gap-4">
          <p className="Nunito-font font-[600] text-[clamp(14px,12px_+_1vw,20px)] lg:text-[20px] ">
            One More Friend Thousands More Fun!
          </p>
          <p className="Nunito-font font-[900] text-[clamp(14px,12px_+_2vw,30px)] lg:text-[34px] ">
            "Find your furry soulmate at Our Pet Shop."
          </p>
          <button className="flex flex-row p-2 lg:w-[160px] gap-[15%]  justify-center w-[calc(140px_+_5%)] whitespace-nowrap  text-[var(--orange-500)]  rounded-[25px]  bg-[var(--white-1000)] items-center">
            <span className="ms-auto">View All</span>
            <div className="w-[30px] aspect-[1/1] rounded-[50px] bg-[var(--orange-500)] flex flex-row justify-center items-center ">
              <IoIosArrowForward className=" text-[var(--white-1000)]" />
            </div>
          </button>
        </div>
      </section>
      
          <section className="px-[5%]  flex flex-col gap-7 py-20">
        <h1 className="Nunito-font font-[800] text-[45px] text-[var(--blue-1000)] text-center  ">
          Our Blogs
        </h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-x-[5%] gap-y-7">
          {bloglst.map((item) => {
            return (
              <div key={item.id} className="blog-card">
                <div className="w-full aspect-[1/0.65] rounded-xl overflow-hidden">
                  <img
                    src={item.url}
                    alt=""
                    className="w-100 h-100 object-cover"
                  />
                </div>
                <div className="blog-info flex flex-col gap-3 py-2">
                  <h1 className="Nunito-font lg:text-[18px] text-[16px] line-clamp-2 font-extrabold ">
                    {item.title}
                  </h1>
                  <p className="text-[var(--black-500)] text-[14px] line-clamp-3">
                    {item.desc}
                  </p>
                  <button className="bg-[var(--blue-1000)] text-[var(--white-1000)] p-2 rounded-sm w-max">
                    View Details
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </section>
      
       <section id="footer">
        <Footer />
      </section>
    </>
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
