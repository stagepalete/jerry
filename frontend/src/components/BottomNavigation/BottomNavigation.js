import React from 'react';
import Image from 'next/image'
const BottomNavigation = () => {
    return (
        <div className="container w-50 fixed-bottom bg-light rounded mb-2">
            <div className="row justify-content-center align-items-center p-0 m-0" style={{ width: '100%', height: '50px' }}>
                <div className='col-3'>
                    <button className="btn btn-primary btn-lg rounded-circle p-0" style={{ width: '40px', height: '40px' }}></button>
                </div>
                <div className='col-3'>
                    <button className="btn btn-danger btn-lg rounded-circle fs-6 p-0" style={{ width: '40px', height: '40px' }}>SOS</button>
                </div>
                <div className='col-3'>
                    <button className="btn bg-light btn-lg rounded-circle p-0" style={{ width: '40px', height: '40px', backgroundColor: 'white'}}>
                        <Image src='/images/icons/freewifi.webp' 
                        width={30}
                        height={30}
                        color='black'
                        />
                    </button>
                </div>
                <div className='col-3'>
                    <button className="btn bg-light btn-lg rounded-circle p-0" style={{ width: '40px', height: '40px'}}>
                    <Image src='/images/icons/kz.png' 
                        width={30}
                        height={30}
                        color='black'
                        />
                    </button>
                </div>
            </div>
        </div>
    );
};

export default BottomNavigation;
