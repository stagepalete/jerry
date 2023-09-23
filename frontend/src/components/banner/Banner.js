import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS if not already done
import Image from 'next/image'


const Banner = (src, width, height) => {
    return (
        <div id="carouselExampleControls" className="carousel slide" data-ride="carousel">
            <div className="carousel-inner">
                <div className="carousel-item active">
                    <Image
                        src={src}
                        className="d-block w-100 border rounded"
                        width={width}
                        height={height}
                        alt="Image slide"
                    />
                </div>
                <div className="carousel-item">
                    <Image
                        src={src}
                        className="d-block w-100"
                        width={width}
                        height={height}
                        alt="Image slide"
                    />
                </div>
            </div>
        </div>
    );
};

export default Banner;
