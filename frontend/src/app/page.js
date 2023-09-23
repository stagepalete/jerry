// RootLayout.js
"use client"
import 'bootstrap/dist/css/bootstrap.min.css';
import HeaderNavbar from '@/components/header/Navbar';
import Banner from '@/components/banner/Banner';
import Notifications from '@/components/modal/PushNotification'; // Updated import
import BottomNavigation from '@/components/BottomNavigation/BottomNavigation';
export default function RootLayout({ children }) {
  const firstbannerimgsrc = '/images/banner/image1.jpg';
  const secontBannerimgsrc = '/images/banner/image2.jpg';

  return (
    <html lang="en">
      <body>
        <header className="container bg-white">
          <HeaderNavbar />
        </header>
        <main className='bg-white'>
          <div className='container'>
            <Banner src={firstbannerimgsrc} width={720} height={350} />
            <br />
            <h6>Интересное в городе</h6>
            <Banner src={secontBannerimgsrc} width={720} height={350} />

            <div>
              <Notifications />
            </div>

          </div>

        </main>

        <footer>
          <BottomNavigation />
        </footer>
      </body>
    </html>
  );
}
